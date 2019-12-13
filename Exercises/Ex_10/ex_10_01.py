inp = input ('Enter a file name: ')
try:
    h=open (inp)
except:
    print('Invalid input!')
    exit()
d=dict()
li=[]
t=[]
for line in h:
    words=line.split()
    if len(words)==0: continue##skips blanck lines
    if words [0]!='From': continue##skips lines not strating with "From"
    li.append(words[1])
#print (li)
for word in li:
    d[word]=d.get(word,0)+1#This code creates/retrieves/updates values of a counter dictionary
#print (d)
for k,v in d.items():
    #print (k,v)
    t.append ((v,k))
    t.sort(reverse=True)
#print (t)
#print (t[0])
##This loop assigns variable names largest and adress to (v,k) and prints it:
for largest,adress in t[:1]:#t[0] won't work in a loop because not iterable !
    print (adress, largest)
