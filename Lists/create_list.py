a=list()
while True:
    inp=input ('Enter number: ')
    if inp =='done':
        break
    try:
        value = float (inp)
    except:
        print ('Invalid input !')
        continue
    a.append(value)
print (a)
