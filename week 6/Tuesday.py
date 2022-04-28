#for loop is like a robot just asking whats next
# the sequence or data type is driving the for loop

#.split will turn a string into individual words

sentence = "cat, dog, rat, lion, zebra"

words = sentence.split()

word_count = 0 #step 1
for one_word in words: #step 2
    #step 3 do stuff
    word_count = word_count + 1 #step 4
    print (one_word, word_count)

print ("final count", word_count)
#step 5 check your result, this the basic version of a counter





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

#for loops have to answers to receive keep going or stop
#once the the for loops is done iterating through the list of item it stops.
# the for loop on the backend is constantly returning whats next, so you dont have to worry about returing

# 4 steps to a counter
# 1 establish base outside of for loop, DONOT put it inot the for loop
# 2 Start a for loop, do for loop first
# 3 Do the body of the for loop, code that will do whatever you want it to do.
# 4 implement counter into for loop

sentences = "cat dog snake python cars"
words = sentences.split()

word_count = 0  #1
total_letters = 0 # this is for the accumalator #1
for one_word in words: #2 both counter and accumelator
    word_length = len(one_word)#3,
    # at this point sit down and analyze what the next step in the flow of your work
    total_letters = total_letters + word_length # 4 for counter
    word_count = word_count + 1 #4 counter

print ("final countdown", word_count) #check your results
print ("total letters", total_letters) #check your results
print (total_letters/word_count) #average letters per word, check results
