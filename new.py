import json

# Define the alphabet to be used in the cipher for shifting
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Functions to encrypt and decrypt messages
def encrypt(plain,shift,alphabet=alphabet):
    split_words = [x for x in plain.split()]
    for i in range(len(split_words)):
        split_words[i] = ''.join([alphabet[(alphabet.index(letter)+shift)%26] for letter in split_words[i]])
    return ' '.join(split_words)

def decrypt(plain):
    for loops in range(25): 
        shifted_word = encrypt(plain,loops)
        word_list = shifted_word.split()
        valid_count = 0
        for word in word_list:
            with open(f'data/{word[0]}.json', 'r') as file: 
                if word in json.load(file).keys():
                    valid_count += 1
        if valid_count == len(word_list):
            return shifted_word
    return "word could not be decrypted"


# Main program loop gui
import tkinter as tk   
import ttkbootstrap as ttk        
from tkinter import font as tkfont

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Calibri', size=24, weight="bold")
        self.geometry("320x240")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, EncryptionPage, DecryptionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Caeser Cipher", font=controller.title_font)
        label.pack(side="top", pady=10)

        button1 = ttk.Button(self, text="Go to Encryption", 
                            command=lambda: controller.show_frame("EncryptionPage"))
        button2 = ttk.Button(self, text="Go to Decryption",
                            command=lambda: controller.show_frame("DecryptionPage"))
        button1.pack(pady=5)
        button2.pack()


class EncryptionPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Encryption", font=controller.title_font)
        label.pack(side="top", pady=10)

        text_var = tk.StringVar()
        text = ttk.Entry(self, textvariable=text_var)
        text.pack()

        shift_var = tk.IntVar()
        shift = ttk.Entry(self, textvariable=shift_var)
        shift.pack()
        
        encrypt_var = tk.StringVar()
        encrypt_button = ttk.Button(self, text="Encrypt", command=lambda: encrypt_var.set(encrypt(text_var.get().upper(), shift_var.get())))
        encrypt_button.pack(pady=5)

        encrypt_label = ttk.Label(self, textvariable=encrypt_var, font="Calibri 12")
        encrypt_label.pack()

        button = ttk.Button(self, text="Go to the decryption page",
                           command=lambda: controller.show_frame("DecryptionPage"))
        button.pack(side="bottom", pady=10)


class DecryptionPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Decryption", font=controller.title_font)
        label.pack(side="top", pady=10)

        entry_frame = ttk.Frame(self)
        entry_var = tk.StringVar()
        entry = ttk.Entry(entry_frame, textvariable=entry_var)
        entry.pack()
        decrypt_var = tk.StringVar()
        decrypt_button = ttk.Button(entry_frame, text="Decrypt", command=lambda: decrypt_var.set(decrypt(entry_var.get().upper())))
        decrypt_button.pack()
        entry_frame.pack()

        decrypt_label = ttk.Label(self, textvariable=decrypt_var, font="Calibri 12")
        decrypt_label.pack(pady=5)
        button = ttk.Button(self, text="Go to encryption page",
                           command=lambda: controller.show_frame("EncryptionPage"))
        button.pack(side="bottom", pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
