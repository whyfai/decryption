import json
import time

start_time = time.perf_counter()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
        with open(f'data/{shifted_word[0]}.json', 'r') as file:
            words_dictionary = json.load(file)
            file.close()
        for decrypted_word in words_dictionary.keys():
            if decrypted_word == shifted_word:
                return print(shifted_word.lower())
    return print("word cannot be decrypted")

decrypt('GBSB')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")