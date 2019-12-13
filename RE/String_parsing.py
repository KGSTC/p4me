# Extracts a substring inside a string using Find and string slicing:
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos= data.find ('@')
print (atpos)
sppos =data.find (' ',atpos) #Finds the position of a character in a string, with argument 'after atpos position'
print (sppos)
host = data [atpos+1:sppos]
print (host)
print ('End of task1')
#Extracts a substring inside a string using splitting the line into shunks and shunk of intrest into strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = data.split ()
email = words [1]
print (email)
pieces = email.split('@')
print (pieces [1])
print ('End of task2')
#Extracts a substring inside a string using regular expression
import re
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
x= re.findall ('\S+@(\S+) ',data) #Or: re.findall('@([^ ]*)'), [^ ]<=>Non-blank, *Matchs many of them (0 or more) and stops only when meets a white space
print (x)
print (x[0])
print ('End of task3')
#Extracts a substring inside a string using regular expression, in chosen lines:
import re
data= 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
x=re.findall ('^From .*@([^ ]*)',data)
print (x)
print (x[0])
print ('End of task4')
#Spam confidence:
import re
hand = open ('sample_short.txt')
numlist=[]
count=0
sum=0
for line in hand:
    line=line.rstrip()
    x=re.findall ('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len (x)!=1: continue #skips the next code for lines that don't match when x is empty !=1
    num=float (x[0])
    numlist.append (num)
    count=count+1
    sum=sum +num
print ('Maximum:', max (numlist))
print ('Average:', sum/count)
