import string
inp=input('Enter file: ')
try:
    h=open (inp)
except:
    print ('Invalid input !')
    exit()
d={}
t=[]
for line in h:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()#List of words
    for k in words:
        d[k]=d.get(k,0)+1# dictionary (word,count)
#print (d)
#print(d.items())##Prints a tuple of d contents.
#t=list(d.items())# Creates a list of dict_list elements. dict_list is a tuple and not a list. Tuples cannot be sorted.
#print (t)
for k,v in d.items():
    t.append ((v,k))
#print (t)
t.sort(reverse=True)
#printt2[0:9])
for v,k in t[:10]:
    print (v,k)
    #t2.append (k)
#print (t2)
