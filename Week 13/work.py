# hw 4 uses nested loops and dictionary accumolators
# Dicts are not an offshot of lists, they're a completley different thing.
#create a dict cheat sheet for syntax
#everytime you are unsure if the syntax, look up on your cheat sheet
#remind yourself or returners and mutators
#look at prof notes on dicts for cheat sheet stuff
#core patters for dicts are in the books

#empty_dict = {} #dict
# {'one'(key):0 (value)}
#can prepoluate dicts
#count_us ={'one': 0, 'two': 0, 'three':0}
#vs
#one =0
#two =0
#three = 0
#can iterate over a list
#data types allowed for keys, are data types thare unmutable. So generally strings
#grades = {'945':[30,30,30,30,30]}
#you can use variables for values
#all values data types should be the same\
#10;37 for advances dict examples

#look up student 945

#print(grades[945])
#print (type(grades['945']))

#add student 950
#print (grades)
#grades['950'] = [25, 25, 30, 30, 30] # setting up one pair
#print (grades)

#for key in grades:
  #print(key,grades[key])
  #student_id= key
  #student_grades = grades[student_id]
 # hw1 = student_grades[0]
  #print (student_id, student_grades, hw1)

##
  #big_gradebook = {}
#many_students = ['945','950','951','952','988']

#prepopulate the dict with each student getting an empty list
 # general idea of HW 4
#for s_id in many_students:
  #big_gradebook[s_id] = []

#print (big_gradebook)

# when you print keys, the keys need to be verbatum

#count_us = {'one' : 4, ' two' : 50, 'three' : 300}
#print (count_us['two'])
#count_us['four'] = 1000
#count_us ['four'] = 9000

#for key in count_us:
#  value = count_us[key] #can print a specific key but have to know the key
 # print (key, value)

#counter in a dictinonry

# counts = {}
#
# vowels = ['a', 'o', 'e', 'u', 'i', 'y']
# #known keys prepopulate, will only work if the keys are already in there
#
# for c in vowels:
#   counts[c]=0
#
# print (counts)
#
# text = 'Pomona College is a private liberal arts college in Claremont, California. It was established in 1887 by a group of Congregationalists who wanted to recreate a "college of the New England type" in Southern California.'
#
# for c in text:
#   c = c.lower
#   if c in vowels:
#     counts[c] = counts[c] + 1
#
# print (counts)
#
# character_counts = {}
#
# for c in text:
#   c = c.lower
#   if c in character_counts:
#     character_counts[c] = character_counts[c] + 1
#   else:
#     character_counts[c] = 0
#
# print (character_counts )
#
# letters = [ 'a', 'p']
#
# for letter in letters:
#   out = open (letter + '.txt', 'w', encoding = 'utf-8')
#   for t in text:
#     t = t.lower()
#     if letter == t:
#       outfile.write (t + \n)
#   outfile.close()
#
