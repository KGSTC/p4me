inp = input ('Enter a file name: ')
try:
    h=open (inp)
except:
    print('Invalid input!')
    exit()
d=dict()
li=[]
for line in h:
    words=line.split()
    if len(words)==0: continue##skips blanck lines
    if words [0]!='From': continue##skips lines not strating with "From"
    li.append(words[1])
#print (li)
for word in li:
    d[word]=d.get(word,0)+1#This code creates/retrieves/updates values of a counter dictionary
print (d)
