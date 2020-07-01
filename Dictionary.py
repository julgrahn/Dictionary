import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userInput = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if userInput == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif userInput == 'N':
            return word + " didn't match any word. Sorry!"
        else:
            return "Wrong input. Try again!"       
    else:
        return "The word does not exist. Please try again."

word = input("Enter word: ")

output = meaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)