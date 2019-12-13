num_list=[]
while True:
    inp = input ('Enter a number: ')
    if inp == 'done':
        break
    try:
        value=float (inp)
    except:
        print('Invalid input')
    num_list.append (value)
print ('Maximum: ', max (num_list))
print ('Minimum: ',min (num_list))
