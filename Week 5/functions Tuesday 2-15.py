# functions 9:54
# Functions are weird but are very useful
# get syntax right
# when you use a fucntion you can call it, meaning use it
# defining a function is telling python what the function should do
# if you define it but dont call it nothing will happen
# def is short for define, def creates a def block just how if creates a if block.
# the syntax for functions is very flexiable

# def take_270():
#     print  ( "Ill let you know if you can take 270")
#
# take_270()
#
# def take_380():
#     #print (True)
#     result = True
#     # doing more stuff ...
#     return True
# return is not a func, does not paranthesis
# the return is needed so the if statement can be executed
# return is a key word that allows the func to communicate back to the main func, a func is basically like it's own little world

# print (take_380())

# 10: 34 rules of return: return is specials, not a func, return should be the last line in your func definition,
# while starting out try to have only one return at end of the func, as soon as the func reaches return the func is executed and it's done.
# does not matter how many other lines there are after the return
# do not reuse variable names in func and the main program
# its normal to define func at the beginning of the program, and use them later on
# if take_380() == True:
#     print ("congrats")

# in funcs print = scream and return = save
# return goes in the last line of the func
# for calling func the variable name doesn't matter just the order in which values are passed into the func
# Ex:

def take_450( taken_208, taken_209):
    if taken_208 and taken_209:
        result = True
    else:
        result = False
    print ("completed check")
    return result

stu_has_208 = True
stu_has_209 = False

if take_450( stu_has_208, stu_has_209):
    print ("congrats")
else:
    print ( " error ")  # here python just passed the boolean values in order in which they're established, the variable name did not matter


