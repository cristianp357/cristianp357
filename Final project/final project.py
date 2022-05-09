import string
import json

def word_finder(words):
    for characters in string.punctuation:
        words = words.replace(characters, "")
        finished_words = words.strip()

    return finished_words

def word_seeker(original_string, cap_seeker):
    original_string = original_string.upper()
    cap_seeker = cap_seeker.upper()

    original_string = word_finder(original_string)

    order = original_string.split()

    result = cap_seeker in order

    return result


look_ups = ['dracula', 'night', 'castle']

spooky_dict = {}

fname = 'Dracula.txt'

spooky_dict['source_material'] = fname
spooky_dict['inquiries'] = len(look_ups)

for ups in look_ups:
    spooky_dict[ups] = {"instances": 0, "sentences": []}

infile = open(fname, 'r', encoding='utf-8')

sentences = infile.readlines()
infile.close()

for sentence in sentences:
    for ups in look_ups:
        if word_seeker(sentence, ups):
            spooky_dict[ups]['instances'] += 1
            print(ups, "instances are", spooky_dict[ups]['instances'])

            spooky_dict[ups]['instances'] = spooky_dict[ups]['instances'] + 1
            print (ups, "sentences are", spooky_dict[ups]['sentences'])

            spooky_dict[ups]['sentences'].append(sentence)
            print(spooky_dict[ups]['instances'], len(spooky_dict[ups]['sentences']))


print (spooky_dict)

fileout = open('dracula_searches.json', 'w', encoding='utf-8')
json.dump(spooky_dict, fileout, indent=4)
fileout.close()
