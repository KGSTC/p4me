#This code asks for a file, reads the file and looks for lines starting with a particular string:
file_name=input ('Please enter file name: ')
try: ## To catch an input error: Try/Except ==>Protecting the open call
    handle = open (file_name)
except:
    print ('Please entre a valid file name in text_files directory.')
    exit() ### Exit function terminates the program
count=0
for line in handle:
    line = line.rstrip () ## This method deletes \n 'newline'=> wipes white space after (=r) a string
    if line.startswith ('From'):
        print (line)
        count =count +1
print ('There are', count, ' emails in this file.')
#This code asks for a file, finds and counts lines where a search string is anywhere in the line within another string:
file_name=input ('Please enter file name: ')
try:
    handle = open (file_name)
except:
    print ('Please entre a valid file name in text_files directory.')
    exit()
count =0
for line in handle:
    line = line.rstrip ()
    if line.find ('@uct.ac.za')==-1: continue
    print (line)
    count =count+1
print ('There are', count, 'lines, containing : @uct.ac.za, in this file.')
# This code asks for a file and returns the position of a string within a string in the line:
file_name=input ('Please enter file name:')
try:
    handle = open (file_name)
except:
    print ('Please entre a valid file name in text_files directory.')
    exit()
for line in handle:
    line = line.rstrip ()
    position= line.find ('@uct.ac.za')
    if line.find ('@uct.ac.za')==-1: continue
    print (position, ' : ', line)
