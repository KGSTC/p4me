import re
inp=input ('Enter a regular expression: ')
hand = open ('mbox.txt')
count =0
for line in hand:
    line=line.rstrip()
    x=re.findall (inp, line)
    if len(x)!=1: continue
    count=count+1
print ('mbox.txt had', count, 'lines that matched', inp)
