import re
ls1=[]
count=0
hand = open ('regex_sum_254350.txt')
for line in hand:
    line=line.rstrip()
    x=re.findall('([0-9]+)',line)
    if len(x)<=0: continue
    #print (x)
    ls1=ls1+x
#print (ls1)
ls2=[int(i) for i in ls1]
print ('The sum of numbers in text is: ', sum(ls2))
