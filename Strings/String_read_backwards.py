#This code reads a string backwards and assign an index number to each letter:
word= input ('Please enter word: ')
length = len (word)
index = length -1
for letter in word:
    print (index, word [index])
    index =index -1
#This code reads a string backwards and assign an index number to each letter:
word= input ('Please enter your name: ')
length = len (word)
index = length -1
while index in range (length):
    print (index, word[index])
    index = index-1
