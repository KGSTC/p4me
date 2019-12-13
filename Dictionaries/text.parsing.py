#This code counts the occurence of words in a punctuated text
#and prints the keys in alphabetical order:
import string
inp = input ('Enter file: ')
try:
    h=open (inp)
except:
    print ('Invalid file name!')
    exit()
d=dict()
for line in h: #reading each line in the text
    line=line.rstrip ()##preparing the line: rstrip+translate+lower methods
    line=line.translate (line.maketrans ('','',string.punctuation))
    line=line.lower ()
    words=line.split()##splitting line into words
    for word in words:
        #if word not in d:
        #    d[word]=1
        #else:
            #d[word]+=1# same as d[word]=d[word]+1
        d[word]=d.get(word,0)+1
print (d)
lis=list(d.keys())# Creates a list (ordonnee) of the words (keys) in dictionary d
print (lis)
lis.sort()#sorting words in alaphabetical order
for key in lis:
    print (key,d[key])
