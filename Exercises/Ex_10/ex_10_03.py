#This code removes punctuation and digits and capital letters in a text. Then counts the number of each letter. Finally the letters are given in descending order of use.
import string
d={}
l=[]
lst=[]
inp=input ('Enter a file name: ')
try:
    h=open (inp)
except:
    print ('Invalid input !')
    exit ()
for line in h:
    line = line.translate (str.maketrans('','',string.punctuation))#Removes punctuation from lines
    line = line.translate (str.maketrans('','',string.digits))#Removes digits from lines
    line=line.lower()
    words=line.split()
    #print (words)
    for word in words :
        letters=list(word)
        #print (letters)
        for letter in letters:
            l.append (letter)
#print (l)
for k in l:
    d[k]=d.get (k,0)+1
#print (d)
for k,v in d.items():
    lst.append((v,k))
lst.sort(reverse=True)
for k,v in lst:
    print (v,k)
