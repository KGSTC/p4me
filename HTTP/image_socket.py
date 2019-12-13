# This code requests an image file from a web server (or mail server (port 21), and other servers) using HTTP application protocol:
import socket
import time

## This part creates a socket in order to be connected to the www.pr4e.org server on port 80
HOST= 'data.pr4e.org'
PORT=80
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST,PORT))# or 'data.pr4e.org',80)
#This part accumulates the data in a string
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')#b'...' literals = a sequence of octets (integers between 0 and 255) wheras a'string' = a sequence of Unicode characters (UTF-16 or UTF-32, depending on how Python was compiled)
count= 0                                                                #b'string' <=> 'string'.encode()
picture=b" "
while True:
    data= mysock.recv(5120)
    if len(data)< 1: break
    time.sleep (0.25) #==> slows down our successive recv(), so that the server can get ahead of us and send more data before the next call recv() and therefore get 5120 characters we ask for, except for the first and last calls.
    count = count + len (data)
    print (len(data), count)
    picture = picture +data
####This part closes the socket of communication
mysock.close()
#Look for the end of the header (2 CRLF)
pos= picture.find (b"\r\n\r\n")
print ('Header length', pos)
print (picture [:pos].decode())

#Skip past the header and save the picture data in a file
picture = picture [pos+4:]
fhand = open ("stuff.jpg", "wb")
fhand.write (picture)
fhand.close
print ('done !')
