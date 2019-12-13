handle= open ('sample_short.txt')
for line in handle:
    line=line.rstrip()
    if line.startswith ('From '):
        print (line)
        word_list= line.split ()
        print (word_list[2])
print ('Done !')
