import json


def dictionary_fetch (key):
    """ this function d'fetch a dictionary definition"""
    # with json.load(open('UdemyDictionaryData.json')) as data:     # python did not like this
    #     return data[key]
    data = json.load(open('UdemyDictionaryData.json'))  # could be from an API

    key = key.lower()

    try:
        if key in data:
            return data[key]
    except KeyError:
        return 'No entry found for this word'


# print(dictionary_fetch('rain'))
word = input('Please enter word: ')
print(dictionary_fetch(word))

