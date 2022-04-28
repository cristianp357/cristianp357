sentence1 ='there are many desks here'
sentence2 = 'also some chairs and bricks'

word1 = sentence1.split()
word2 = sentence2.split()

alllines = []
word1.append('HELLO')
alllines.append(word1)
alllines.append(word2)

print (alllines)
allwords = word1 + word2

print (allwords)

firstletters = [] #step 1: create an empty list for the append

for w in word1: #step 2
    firstletters.append(w[0]) #step 3 and step 4: find the thing. 0 refers to the first letter in each word in the list.
    #step 5 use append

print (firstletters)
