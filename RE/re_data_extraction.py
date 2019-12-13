#Searches for shunks of text with an @ sign in the middle=email:
import re
s='A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst1 = re.findall ('\S+@\S+',s)#\S: non white character, #\s+: one or more non white character
print (lst1)
print ('End of task 1')
print ('')
#Searches for any shunks of text with an @ sign :
import re
s='A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst2= re.findall ('\S*@\S*',s) # \S* : zero or more non-blank character. * applies to the immediate on the left character
print (lst2)
print ('End of task 2')
print ('')
# Searches for strings that have an @ sign between character:
import re
hand = open ('sample_short.txt')
for line in hand:
    line = line.rstrip()
    x= re.findall('\S+@\S+',line) # \S+ : one or more non-blank character. + applies to the immediate on the left character
    if len(x)>0: # if list is not empty print list
        print (x)
print ('End of task 3')
print ('')
#Searches for expressions that start with any letter or number, followed by sign '@',
#followed by zero or more non-blank character, followed by any letter <=> Email address
import re
hand = open ('sample_short.txt')
for line in hand:
    line = line.rstrip()
    y= re.findall ('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line) # \S* : zero or more any non-blank character
    if len (y)>0:
        print (y)
print ('End of task 4')
print ('')
