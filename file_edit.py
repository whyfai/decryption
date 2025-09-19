import json

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

for i in alphabet:
    with open(f'data/{i}.json', 'r+') as file:
        words_dictionary = json.load(file)
        for key in words_dictionary.keys():
            words_dictionary[key] = 1
        file.seek(0)
        json.dump(words_dictionary, file)
        file.truncate()
        file.close()