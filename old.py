import json
import time

start_time = time.perf_counter()

with open(f'words_dictionary.json', 'r') as file:
    words_dictionary = json.load(file)
    file.close()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(alphabet,plain,shift):
    temp = []
    for i in range(len(plain)):
        index = alphabet.index(plain[i])
        if index + shift>25:
            temp.append(alphabet[index+shift-26])
        else:
            temp.append(alphabet[index+shift])
    return ''.join(temp)

def decrypt(word):
    for loops in range(26):
        shifted_word = encrypt(alphabet,word,loops)
        for decrypted_word in words_dictionary.keys():
            if decrypted_word == shifted_word:
                return print(shifted_word.lower())
    return print("word cannot be decrypted")

decrypt('gbsb')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")