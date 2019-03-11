import json
import difflib
from difflib import SequenceMatcher, get_close_matches


def dictionary_fetch (key):
    """ this function d'fetch a dictionary definition"""
    # with json.load(open('UdemyDictionaryData.json')) as data:     # python did not like this
    #     return data[key]
    data = json.load(open('UdemyDictionaryData.json'))  # could be from an API

    key = key.lower()
    close_matches = get_close_matches(key, data, cutoff = 0.8)

    try:
        if key in data:
            return data[key]
        elif len(close_matches) > 0:
            # return 'Did you mean %s?' % get_close_matches(key, data, cutoff=0.8)[0]
            prompt_string = f'Did you mean {close_matches[0]} instead ? (\'Y\' for Yes \'N\' for No)'
            retry = input(prompt_string)
            if retry.lower() == 'y':
                return data[close_matches[0]]
            else:
                return 'Unsure regarding this word - please check'
        else:
            return 'No entry found for this word - please check'
    except KeyError:
        return 'No entry found for this word - please check'
    # except:
    #     return 'Error occurred'


# print(dictionary_fetch('rain'))
word = input('Please enter word: ')
print(dictionary_fetch(word))

