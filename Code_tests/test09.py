#This code sorts the words in a text from the longest to the shortest:
txt='Je suis belle et intelligente'
words=txt.split()
print (words)
t1=list () #Gives an error with tuples, as tupples don't support the append method
for word in words:
    t1.append ((len(word),word))#Item (len(word),word) is the argument of the method append of list t
print (t1)
t1.sort(reverse=True)#Sorts the list in decreasing order/ first element of item, second ...
print (t1)
t2=list()
for length,word in t1:
    t2.append (word)
print (t2)
##Otherwise a dictionary can be used instead of lists to sort a list of words in decreasing order
d = {key: len(key) for key in txt.split()}
print (d)
t3=list()
for k,v in d.items():
    t3.append((v,k))
t3.sort(reverse=True)# Or t3.sorted (t3,reverse=True)
print (t3)
