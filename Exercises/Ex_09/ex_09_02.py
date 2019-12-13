inp=input ('Enter a file name: ')
try:
    h=open (inp)
except:
    print ('Invalid input!')
    exit()
d=dict()
words_list=[]
for line in h:
    #line=line.rstrip()## Not needed when using list words indexes instead of line.startswith()
    words=line.split()
    if len(words)==0 : continue##Skips blank lines (without words) and avoids code error: words[0] out of range
    if words[0] != 'From': continue##skips lines starting with other words than 'From'
    #print (words[2])
    words_list.append (words [2])
#print (words_list)
for word in words_list:
    d[word]=d.get (word,0)+1##Replaces "if word not in d: d[word]=1 else: d[word]+=1"
print (d)                   ###That's how new enteries are created and enteries are updated in dic
