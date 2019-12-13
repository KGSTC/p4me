# In case of short files: this code reads the whole file:
handle=open('sample_short.txt')
inp = handle.read()
print (len(inp))
print (inp [:20])
# In case of large files: this code reads the file line by line (for each iteration of the for loop) and discard it (doesn't store in the main memory) before moving to the next line:
handle=open('sample_large.txt')
count=0
for line in handle:
    count =count +1
print ('There are', count, ' lines in this file.')
