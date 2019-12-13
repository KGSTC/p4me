#This code sorts strings according to lexical order:
## Upper case and lower case comparison depends on character set of each computer.
###Please, check it first. On this laptop Uppercase comes before lowercase.
word = input ('Please enter word ')
if word < 'banana':
    print ('Your word,', word, ', comes before banana.')
elif word > 'banana':
    print ('Your word,', word, ', comes after banana')
else:
    print ('All done !')
x=max (word)
y=min (word)
print (word, 'Your largest letter is:', x,'Your smallest letter is: ', y)
