# Search for lines that start with 'X-' followed by any non-blank character and ':',
# followed by a space and any number.The number can include a decimal
# returns lists composed of 1 string ; X-gftdf: 0.87676
import re
hand = open ('sample_short.txt')
for line in hand:
    line= line.rstrip()
    x=re.findall ('^X-\S*: [0-9.]+',line)# or ('^X-.*: [0-9.]+') .*: zero or more character, a space : space, [0-9.]: any number followed or not by decimals
    if len (x)>0:
        print (x)
print ('End of task1')
print ('')
#Search for lines that start with 'X-' followed by any non-blank character and ':',
# followed by a space and any number.The number can include a decimal
# returns a of list strings ; X-gftdf: 0.87676
import re
hand = open ('sample_short.txt')
for line in hand:
    line= line.rstrip()
    if re.search ('^X-\S*: [0-9.]+',line):# or ('^X-.*: [0-9.]+') .*: zero or more character, a space : space, [0-9.]: any number followed or not by decimals
        print (line)
print ('End of task2')
print ('')
#Search for lines that start with 'X-' followed by any non-blank character and ':',
# followed by a space and any number.The number can include a decimal
# returns lists composed of 1 string ; X-gftdf: 0.87676
import re
hand = open ('sample_short.txt')
for line in hand:
    line= line.rstrip()
    x=re.findall ('^X-\S*: ([0-9.]+)',line)# ([0-9.]+): () indicates the segment of the string of interest
    if len (x) > 0:                        # Period '.'= any single character except \n newline. If '.' inside brackets, '.' = period (point decimal).
        print ('\n'.join(x)) #  convert a Python list of strings (or any other iterable such as a tuple) to a string for display.
print ('End of task3')        ## Or print (',  '.join(x)) without return to newline ==> string1, string2, sting3, ...
print ('')
#Search for lines that start with 'Details:' and end with rev= number
#Extract only the number at the end of lines
import re
hand = open ('sample_short.txt')
for line in hand:
    line= line.rstrip()
    x=re.findall ('^Details:.*rev=([0-9]+)',line)# ([0-9]+): () indicates the segment of the string of interest
    if len (x) > 0:
        print (x)
print ('End of task4')
print ('')
#Search for lines that start with 'From ' and end with rev= number
#Extract only the number at the end of lines
import re
hand = open ('sample_short.txt')
for line in hand:
    line= line.rstrip()
    x=re.findall ('^From .* ([0-9][0-9]):',line)
    if len (x) > 0:
        print (x)
print ('End of task5')
print ('')
# Seraches for amounts of money in dollars'$'
x='You have just received $100.00 for cookies.'
y=re.findall ('(\$[0-9.]+)',x)# adding '\' before a special character, cancel its "specialness". '$' = at the end of string. But \$ = dollars $
if len (y)>0:                 # the period inside [] means just '.' and not any character
    print (y)
    print ('\n'.join(y))
print ('End of task6')
print ('')
