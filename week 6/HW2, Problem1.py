import string

def clean_punc(dirty_string):
    for punc_character in string.punctuation:
        dirty_string = dirty_string.replace(punc_character, "")

    return dirty_string

t1 = "***START OF THE PROJECT GUTENBERG EBOOK THREE YEARS IN EUROPE***"
t2 = "E-text prepared by Suzanne Shell, Michael Punch, and the Project Gutenberg"
t3 = "MEMOIR OF WILLIAM WELLS BROWN,                           _Page_ ix-xxix"

print(clean_punc(t1))
print(clean_punc(t2))
print(clean_punc(t3))


