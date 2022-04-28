# words = [ 'cat', 'dog', 'horses']
#
# word_counts = {}
#
# for word in words:
#     word_counts[word] = []
#
# print (word_counts)

# sentence = "Hello, are you a Human?"
# words = sentence.split()
# lower_words = []
# for w in words:
#     lower_words.append(w.lower())
# print(lower_words)

# def lower_words(sentence):
#     words = sentence.split()
#     lower_words = []
#     for w in words:
#         lower_words.append(w.lower())
#     return lower_words
#
#
# print(lower_words("Hello, are you a Human?"))

# sentence = "Hello, are you a Human?"
# words = sentence.lower()
# words = words.split()
# word_counts = {}
# for w in words:
#     if w in word_counts:
#         word_counts[w] = word_counts[w] + 1
#     else:
#         word_counts[w] = 1
# print(word_counts)

import string

def clean_punc(dirty_string):
    lists = dirty_string.split()
    lower_words =[]
    for punc_character in lists:
        clean_string = punc_character.strip(string.punctuation)
        clean_string = lower_words.append(clean_string)

    return clean_string

wordle = ("mary, had$ a little lamb. her name was jeff! she can't or won run")
print (clean_punc(wordle))

#dirty_string = dirty_string.replace(punc_character, "")
        #clean_string = dirty_string.strip()
