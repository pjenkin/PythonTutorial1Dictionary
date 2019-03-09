import json


def dictionary_fetch (key):
    """ this function d'fetch a dictionary definition"""
    # with json.load(open('UdemyDictionaryData.json')) as data:     # python did not like this
    #     return data[key]

    data = json.load(open('UdemyDictionaryData.json'))
    return data[key]


# print(dictionary_fetch('rain'))
print(dictionary_fetch('rain'))
