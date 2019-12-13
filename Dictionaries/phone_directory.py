#This code prompts enteries and adds them to a directory:
directory={}
while True:
    i=input ('Do you have more enteries or are you done?  ')
    if i != 'done':
        first=input ('Please, enter first name: ')
        last = input ('Please, enter surname: ')
        number= input ('Please, enter number: ')
        directory[last,first]=number
        for last,first in directory:#the tuple (last, first) is the key in dictionary 'directory'
            print (first,last,directory [last,first])
        print (directory)
        continue
    else:
        print ('Done!')
        exit()
