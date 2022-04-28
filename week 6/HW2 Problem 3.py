import string

def clean_punc(dirty_string):
    for punc_character in string.punctuation:
        dirty_string = dirty_string.replace(punc_character, "")

    return dirty_string

def detect_word (source_string, word_detect):
    source_string = source_string.lower()
    word_detect = word_detect.lower()

    source_string = clean_punc(source_string)

    word_list = source_string.split()
    result = word_detect in word_list
    return result

t1 = "I worked on a project."

print (detect_word(t1, "project"))
