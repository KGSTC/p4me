file_name= input ('Enter a file name ')
handle = open (file_name)
inp= handle.read()
print (inp.upper ())
