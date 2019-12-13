#This code counts how many times an item appears in a list (Histogram/Frequency):
counts=dict()
names= ['Ali', 'Joy', 'Joy', 'zoe', 'Ali', 'Ali' ]
for name in names:
    if name not in counts:
        counts[name]= 1
    else:
        counts[name]=counts[name]+ 1
print (counts)
# This code counts how many times each character appears in a string:
string =input ('Enter text:')
counts ={}
for c in string:
    if c not in counts:
        counts[c]=1
    else:
        counts [c]=counts [c]+1
print (counts)
# Or we could use the method 'get' in dictionaries:
string =input ('Enter text:')
counts ={}
for c in string:
    counts[c]=counts.get (c,0)+1##"counts.get (c,0)"<==>collapsed to line 14 - line 16
print (counts)
