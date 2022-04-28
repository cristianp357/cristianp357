# will be using for loops alot more than while loops
#for loops are definite loops, meaning there's a deffinate humber if stuff.
#syntax  for "for" loops is as follows: for ---- in ---- sequence :
#                                              do stuff

#for ____ in words: this is where you name a variable that will be created
#      do stuff

# animals = ["cats", "birds", "lion", "dog"]
#
# for a in animals:
#     print (a)

# print ("cat")

#for loop is like a robot just asking whats next
# the sequence or data type is driving the for loop

#.split will turn a string into individual words

# sentence = ['cat', 'dog', 'mouse', 'rat']
sentence = ("cat dog snake python cars")

words = sentence.split()

word_count = 0 #step 1
for one_word in words: #step 2
    #step 3 do stuff
    word_count = word_count + 1 #step 4
    print (one_word, word_count)

print ("final count", word_count)
#step 5 check your result, this the basic version of a counter
