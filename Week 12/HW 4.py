import string

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


infile = open ('Three-years-in-europe (5).txt', 'r', encoding='utf-8')

lines = infile.readlines()
infile.close()

word_count = 0


search_terms = ['cat', 'london', 'horse'] #1b: step 1

count_dict = {'cat': 0, 'london': 0, 'horse': 0}

for word in search_terms:
    outfile = open (  word + '-file.txt', 'w', encoding='utf-8')
    word_count = 0
    count_dict = {}
    for line in lines:
        if detect_word(line, word):
            print ('True')
            print (line)
            word_count = word_count + 1
            count_dict[word] = count_dict[word] + 1
            outfile.write(line + '\n')
    outfile.close()
    print(word_count)

print (word, count_dict[word])


