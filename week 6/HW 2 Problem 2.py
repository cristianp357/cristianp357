import string

def clean_punc(dirty_string):
    for punc_character in string.punctuation:
        dirty_string = dirty_string.replace(punc_character, "")

    return dirty_string

def detect_word (source_string, word_detect):
    source_string = source_string.lower()
    word_detect = word_detect.lower()
    word_list = source_string.split()
    result = word_detect in word_list
    return result

t1 = "***START OF THE PROJECT GUTENBERG EBOOK THREE YEARS IN EUROPE***"
t2 = "E-text prepared by Suzanne Shell, Michael Punch, and the Project Gutenberg"
t3 = "MEMOIR OF WILLIAM WELLS BROWN,                           _Page_ ix-xxix"
t4 = "I worked on a project."

print(detect_word(t1, 'project'))
print(detect_word(t2, 'project'))
print(detect_word(t3, 'project'))
print(detect_word(t1, 'projects'))


