# This code searches for lines that contain 'From':
import re
hand = open ('sample_short.txt')
for line in hand:
    line=line.rstrip ()
    if re.search ('From:',line): # Equivalent to : "if line.find ('From:'):""
        print (line)
print ('End of task 1')
print ('')
#Search for line that starts with "From:":
import re
hand = open ('sample_short.txt')
for line in hand :
    line=line.rstrip()
    if re.search ('^From:',line): # Equivalent to : "if line.startswith ('From:'):""
        print (line)             # Equivalent to : re.search ('^F..m:', line)
print ('End of task 2')
print ('')
#Search for line that starts with "From:" and have an "@" sign:
import re
hand = open ('sample_short.txt')
for line in hand :
    line=line.rstrip()
    if re.search ('^F..m:.+@',line):
        print (line)
print ('End of task 3')
print('')
