#This code modifies a list 't' and returns the same modified list 't':
def delete_head (t):
    del t[0]
t1=[1,2,3]
delete_head (t1)
print (t1)
# This code processes a list 't' and creates another list with required modifications:
def tail (t):
    return t[1:]
t1=[1,2,3]
t2=tail(t1)
print (t2)
# This code modifies a list:
t1=[100,2,3,4,100]
t2=[100,5,6,7,100]
def chop (t):
    del t[0]
    del t[len (t)-1]
chop (t1)
print (t1)
#This code creates a new list:
def middle (t):
    return t[1:len(t)-1]
t3=middle (t2)
print (t3)
#This code makes a copy of a list before using a method'sort' to modify it:
orig=t2[:]
t2.sort()
print (t2)
print (orig)
