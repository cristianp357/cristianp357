#when it comes to files python works in more low level langauge way
#three steps to opening files in python
#Tell python that there is a file
# different modes of intereacting with files
# theres like 9 different modes but for this class, only r = read and w = write
#each mode has different mothods available to them
#need to use .close files for all modes in order to save changes to files
#for windows you need to include encoding = 'utf-8'

# infile = open ('Three-years-in-europe-.txt', 'r', encoding = 'utf-8') #step 1
# all_the_text = infile.read() #step 2
# infile.close() #step 3
#
# lower_text = all_the_text.lower ()
#
# outfile =open('3yearslower.txt, 'w', encoding = 'utf-8') #step 1
# outfile.write(lower.text) #step 2
# outfile.close() #step 3
#
# #how to split byline, find specific words in lines
# lines=all_the_text('\n')
#
# #when you split, split consumes whatever it splits on so in this case spaces, you need add new line again
#
# outfile =open('peoplelines.txt', 'w', encoding = 'utf-8')
# for one_line in lines:
#     if 'people' in one_line.lower()
#       print('heres a line', one_line)
#       outfile.write(one.line + '\n')
#
# outfile.close()

infile = open("Three-years-in-europe (2).txt", 'r', encoding='utf-8')

# for line in infile:
#     print(line)
# all_the_text = infile.read()
#
# infile.close()
