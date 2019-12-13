numlist=list()
while True:
    inp=input ('Enter number ')
    if inp =='done':
        break
    try:
        value = float (inp)
        numlist.append(value)
    except:
        print ('Invalid input !')
average = sum (numlist)/len (numlist)
print (numlist, 'The average is: ', average, '.')
