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
#print (d)
largest=None
for key in d:
    #print (d[key])
    if largest is None or d[key]>largest:
        largest =d[key]
#print (largest)
print (dict((v,k) for k,v in d.items()).get(largest), largest)##This code creates a new dictionary 'dict (v,k)' where keys and values of d are inverted. then gets the new value for the indicated key.
##Another way to get the value:
##bigword=None
##largest=None
#for k,v in d.items():
    #if largest is None or v>largest:
        #largest = v
        #bigword = k
#print (bigword,largest)
