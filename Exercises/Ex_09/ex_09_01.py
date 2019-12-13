#This code reads words from a file and stores them in one dictionary:
handle=open('words.txt')
text=handle.read()
text.strip ()
#words=string.split()#list of words in text
d = {key: None for key in text.split()}#dictionary of words in text
#print (d)
string = input ('Enter string: ')
if string in d:
    print ('Word is in dictionary !')
else:
    print ('Word is not in dictionary !')
