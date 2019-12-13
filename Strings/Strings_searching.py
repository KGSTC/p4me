#This code looks for a substring in a string and returns its position:
## If the substring is NOT found in the string, return  value is -1 !
str=input ('Please enter a string: ')
pos = str.find ('AAA')
print (pos)
#Extracting substring from a string:
data = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'
atpos=data.find ('@')
print (atpos)
sppos = data.find (' ', atpos)
print (sppos)
print (data [atpos+1:sppos])
