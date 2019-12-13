handle = open ('sample_01.txt')
count=0
for line in handle:
    count=count+1
print ('There are',count, ' in this file.')
