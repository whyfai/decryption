import json
import time

start_time = time.perf_counter()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plain,shift,alphabet=alphabet):
    return ''.join([alphabet[(alphabet.index(i)+shift)%26] for i in plain])

def decrypt(word):
    for loops in range(25):
        shifted_word = encrypt(word,loops)
        with open(f'data/{shifted_word[0]}.json', 'r') as file: 
            keys = json.load(file).keys()
        for valid_word in keys:
            if valid_word == shifted_word: 
                return print(shifted_word.lower())
    return print("word cannot be decrypted")

print(encrypt('HELLO',29))
decrypt('KHOOR')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")