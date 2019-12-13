#This code appends decimal numbers found in a string to a list:
a = []
line = "abcd 3455 ijkl 56.78 ij"
for word in line.split():
    try:
        a.append(float(word))
    except ValueError:
        pass
print(a)
#This code appends decimal numbers found in a string to a list:
a=[]
line = input ('Please enter your string ')
for word in line.split():
    try:
        a.append(float(word))
    except ValueError:
        pass
print(a)
# This code extracts decimal number from a string:
line = input ('Please enter your string ')
for word in line.split():
    try:
        a=float(word)
    except ValueError:
        pass
print (a)
