hours=[]
d={}
l=[]
inp=input ('Enter a file name: ')
try:
    h=open (inp)
except:
    print ('Invalid input !')
    exit()
for line in h:
    line.rstrip()
    if line.startswith ('From '):
        words=line.split()
        time = words[5]
        hours.append (time.split(':') [0])
for hour in hours :
    d[hour]= d.get (hour,0)+1
#print (d)
#To sort the dictionary by value:
for k,v in list(d.items()):
    l.append((k,v))
    l.sort()
#print (l)
for k,v in l:
    print (k,v)
