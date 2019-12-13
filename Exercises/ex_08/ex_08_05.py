inp=input ('Enter a file name: ')
count=0
handle= open (inp)
for line in handle:
    if not line.startswith ('From '):
        continue
    count = count+1
    email_list= line.split ()
    sender_name=email_list.pop (1)
    #sender_name = email_list [1:2]
    print (sender_name)
print ('There were',count,'lines in the file with From as the first word' )
