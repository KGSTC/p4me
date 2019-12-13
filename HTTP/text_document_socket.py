# This code requests a text document from a web server (or mail server (port 21), and other servers) using HTTP application protocol:
import socket

## This part creates a socket in order to be connected to the www.pr4e.org server on port 80
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#This part gets the document
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode() ## \n\n=\r\n\r\n: the HTTP protocol says we sould send GET command followed by a blank line. \r\n<=> End of line. \r\n\r\n: nothing between 2 end lines<=>blank line
mysock.send(cmd)                                                      ##Encode: according to HTTP, data can only be sent and received as bytes objects (and not strings). Encode/decode methods convert strings to byte objects.
###This part receives data in 512-character chunks from the socket and prints the data out until there is no more data to read
while True:
    data=mysock.recv(512)
    if len(data)< 1:
        break
    print (data.decode(),end='')##decode: according to HTTP, data can only be sent and received as bytes objects (and not strings). Encode/decode methods convert strings to byte objects.
####This part closes the socket of communication
mysock.close()

##!! Telnet is a web browser application that can be used to hack servers<=> creates the socket:
#need to install Telnet on Mac or pc then:
#==>$ telnet cis.poly.edu 80
#Trying 128.238.26.21...
#Connected to cis.poly.edu.
#Escape character is '^]'.
#==>GET /~ross/ HTTP/1.1
#HOST: cis.poly.edu

#HTTP/1.1 200 OK
#Date: Thu, 12 Dec 2019 13:29:00 GMT
#Server: Apache/2.4.6
#Last-Modified: Mon, 12 Nov 2018 16:25:17 GMT
#ETag: "cf-57a7a257df256"
#Accept-Ranges: bytes
#Content-Length: 207
#Content-Type: text/html; charset=UTF-8

#<head>
#<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
#<meta http-equiv="refresh"content="0;url=http://nyu.edu/projects/keithwross/">
#<title> Automatic Forwarding </title>
#</head>
#Connection closed by foreign host.
