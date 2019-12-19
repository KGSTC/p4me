# Reads any web page:
import socket

## Prompts the user for an URL and retrieves any web page:
url=input ('Enter URL:')
try :
    # Finds the host:
    host=url.split('/') [2]

    # creates a socket
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host,80))

    # Gets the document:
    cmd='GET '+ url+' HTTP/1.0\r\n\r\n'
    #print (cmd)
    mysock.send (cmd.encode())

except:
    print ('Enter a valid URL:')
    exit()

# Receives data:
while True:
    data=mysock.recv(512)
    if len(data)<1:break
    print (data.decode(),end='')
    
mysock.close()
