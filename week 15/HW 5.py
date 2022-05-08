import string
import json

def clean_punc(dirty_string):
    for punc_character in string.punctuation:
        dirty_string = dirty_string.replace(punc_character, "")
        clean_string = dirty_string.strip()

    return clean_string
#
def detect_word (source_string, word_detect):
    source_string = source_string.lower()
    word_detect = word_detect.lower()

    source_string = clean_punc(source_string)

    word_list = source_string.split()
    result = word_detect in word_list
    return result


search_terms = ['cat', 'london', 'horse']

count_dict = {}

fname = 'Three-years-in-europe (5).txt'


count_dict['file_name'] = fname
count_dict['num_terms'] = len(search_terms)

for term in search_terms:
    count_dict[term] = {"count": 0, "lines": []}

infile = open (fname, 'r', encoding='utf-8') #step 1a

lines = infile.readlines()
infile.close()



# for word in search_terms:
#     word_count = 0
#     for line in lines:
#         if detect_word(line, word):

for line in lines:
    for word in search_terms:
        if detect_word(word, line):
            print ('True')
            print (line)
            print(word, "count is", count_dict[word]['count'])
            count_dict[word]['count'] += 1
            count_dict[word]['count'] = count_dict[word]['lines']
            count_dict[term]['lines'].append(line)
            print(count_dict[word]['count'], len(count_dict[word]['lines']))


print (count_dict)

fileout = open('term-results.json', 'w', encoding='utf-8')
json.dump(count_dict, fileout, indent = 4)
fileout.close()
