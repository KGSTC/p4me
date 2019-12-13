print ('hello')
while True:
    line = input ('Are you done?')
    if line == 'done':
        break
    print (line)
print ('Done !')
for i in [5,4,3,2,1] :
    print (i)
print ('Blastoff !')

friends = ['Nabila', 'Nadine', 'Dianera']
while True:
    friend = input ('Enter name:')
    if friend in friends:
        print ('Happy new year', friend)
    else :
        break
print ('Done !')

for friend in friends :
        print ('How are you', friend, '?')
print ('Done !')

print ('Before')
for thing in [9,41,12,17,16]:
    print (thing)
print ('After')
