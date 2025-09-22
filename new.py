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

# Main program loop
while True:
    mode = input("input mode encrypt or decrypt [quit/exit to exit]: ").lower()
    if mode in ['e', 'encrypt']:
        print(encrypt(input("input word to encrypt: ").upper(),int(input("input shift value: "))))
    elif mode in ['d', 'decrypt']:
        print(decrypt(input("input word to decrypt: ").upper()))
    elif mode in ['q', 'quit', 'exit']:
        break
