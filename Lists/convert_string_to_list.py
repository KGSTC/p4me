#This code breakes a string in a list of characters:
inp = input ('Enter string: ')
string_list =list (inp)## list is a built-in function
print (string_list)
# This code splits a string in a list of words:
inp=input ('Enter text: ')
word_list=inp.split()## split is a method in strings
print (word_list)
index=word_list[:1]
print (index)
#This code splits a string in a list of words at a particular character<==> delimeter:
inp=input ('Enter text: ')
word_list=inp.split()## split is a method in strings
print (word_list)
delimiter = '-'
word_list=inp.split (delimiter)
print (word_list)
# This code joins strings in a list and add a delimeter between strings from the list:
word_list=['I','love','you','!']
delimiter =' '
sentence=delimiter.join(word_list)##delimiter is a space
print (sentence)
delimiter = ''
string=delimiter.join(word_list)##deimeter is no space:concatenate strings without space
print (string)
delimiter='_'##Delimiter is a _
string=delimiter.join(word_list)
print (string)
