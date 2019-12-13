# To get the index of a charachter in a string : (index is an integer and starts at 0 !)
# the index [] is an operator that outputs a charachter
fruit = input ('Please enter fruit name ')
# To avoid that index value exceeds the length of a string:
x=6
length = len (fruit) # index value is in range [0,length-1]
if x <= length:
    letter =fruit [0]
    print (letter)
    print (length)
    # The index value can be an expression that is computed:
    w= fruit [x-1]
    print (w)
else:
    print ('X is too big')

# This code gives the index of each of the letters in a string:
index = 0
name = input ('Enter name ')
while index < len (name):
    let = name[index]
    print (index, let)
    index = index+1
# This code outputs index of each letter in a string using a definite loop:
    ##in range function ouputs numbers from 0 to length-1##
name = input ('Enter word ')
length = len (name)
for i in range (length):
    print (i, name [i] )
# This code outputs each letter in a string using a definite loop:
name = input ('Enter word ')
for letter in name:
    print (letter)
