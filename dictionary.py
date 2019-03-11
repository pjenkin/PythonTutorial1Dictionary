import json
import difflib
from difflib import SequenceMatcher, get_close_matches


def dictionary_fetch (key):
    """ this function d'fetch a dictionary definition"""
    # with json.load(open('UdemyDictionaryData.json')) as data:     # python did not like this
    #     return data[key]
    data = json.load(open('UdemyDictionaryData.json'))  # could be from an API

    key = key.lower()

    try:
        if key in data:
            return data[key]
        elif len(get_close_matches(key, data, cutoff = 0.8)) > 0:
            return f'Did you mean {0} instead ?', get_close_matches(key, data, cutoff = 0.8)[0]
            # return 'Did you mean %s?' % get_close_matches(key, data, cutoff=0.8)[0]
    except KeyError:
        return 'No entry found for this word'
    except:
        return 'Error occurred'


# print(dictionary_fetch('rain'))
word = input('Please enter word: ')
print(dictionary_fetch(word))

