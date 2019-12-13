#This code prompts for a file name (large size), extracts the floating point value in each line starting with 'xxx':
file_name= input ('Please enter file name: ')
try:
    handle=open (file_name)
except:
    print ('File cannot be opened:', file_name)
    exit()
count=0
total=0
for line in handle:
    line= line.rstrip()
    if not line.startswith ('X-DSPAM-Confidence:'): continue
    count=count+1
    for word in line.split():## This part of the code extracts one number in a string
        try:
            confidence=float(word)
        except ValueError:
            pass
    #print (count, confidence)
    total = total+confidence
average= total / count
#print ('There are', count, ' lines.\n', 'The average confidence is:', average)
print ('Average spam confidence:',round (average,12))
