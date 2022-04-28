# for letter in "abc": # outer
#     for number in range(5): # inner
#         print(letter, number)

# for number in range(5): # outer
#     for letter in "abc": # inner
#         print(letter, number)



names = ['cat', 'dog', 'horse']
for name in names:
    outfile = open('Three-years-in-europe (3).txt', 'w')
    filename = name + 'txt'
    outfile.write(name)
    print('writing files complete')


outfile.close()
