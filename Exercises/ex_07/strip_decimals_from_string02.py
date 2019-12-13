# This code extracts decimal number from a string:
## It returns the last number found in the string
line = input ('Please enter your string ')
for word in line.split():
    try:
        a=float(word)
        print (a)
    except ValueError:
        pass
#This part tests input
b=2*a
print (b)
