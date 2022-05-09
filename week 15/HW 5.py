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


search_terms = ['cat', 'scream', 'write']

count_dict = {}

fname = 'Three-years-in-europe (5).txt'


count_dict['file_name'] = fname
count_dict['num_terms'] = len(search_terms)

for term in search_terms:
    count_dict[term] = {"count": 0, "lines": []}

infile = open (fname, 'r', encoding='utf-8') #step 1a

lines = infile.readlines()
infile.close()

for line in lines:
    for term in search_terms:
        if detect_word(line, term):
            count_dict[term]['count'] += 1
            print(term, "count is", count_dict[term]['count']) #increment counter for term
            #count_dict[term]['count'] += 1

            count_dict[term]['count'] = count_dict[term]['count'] + 1 #increment the counter
            print (term, "lines are", count_dict[term]['lines'])

            count_dict[term]['lines'].append(line) #incrementing the list of lines
            print(count_dict[term]['count'], len(count_dict[term]['lines']))


print (count_dict)

fileout = open('term-results.json', 'w', encoding='utf-8')
json.dump(count_dict, fileout, indent = 4)
fileout.close()

infile = open('term-results.json', 'r', encoding= 'utf-8')
data = json.load(infile)
infile.close()

print(data ['num_terms']*['count'])
print(data ['scream']['lines'])
print(data['file_name'])


# for look_up in data:
#     if detect_word(look_up, "upon "):
#         print (look_up)
#

