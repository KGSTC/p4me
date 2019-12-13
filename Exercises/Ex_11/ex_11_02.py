import re
hand = open ('sample_short.txt')
ls=[]
count=0
sum=0
for line in hand:
    line=line.rstrip()
    x= re.findall('^New Revision: ([0-9]+)',line)
    if len(x)!=1: continue
    num=float(x[0])
    count=count+1
    sum=sum+num
print ('Average is:', sum/count)
