print ('Hello')
x=5
if x>2 :
    print ('Bigger than 2')
    print ('Still Bigger')
print ('Done with 2')

for i in range (5) :
    print (i)
    if i>2 :
        print ('Bigger than 2')
    print ('Done with i', i)
print ('All done')

print ('Hello again')
x = input ('Enter a number:')
try:
    ix = int (x)
except :
    ix =-1

if ix >0 :
    print ('Nice work')
else:
    print ('Not an integer')
