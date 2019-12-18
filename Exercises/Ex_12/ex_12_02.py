# Reads any web page:
import socket
import urllib.request

## Prompts the user for an URL and retrieves any web page:
url=input ('Enter URL:')
try :
    html=urllib.request.urlopen(url)
except:
    print ('Enter URL:')
    exit()
# Finds the host:
host=url.split('/') [2]
#print(host)
# creates a socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host,80))
# Gets the document:
cmd='GET '+ url+' HTTP/1.0\r\n\r\n'
#print (cmd)
mysock.send (cmd.encode())
count=0
while True:
    data=mysock.recv(512)
    if len(data)< 1: break
    count = count + len (data)
    if count<=3000:
        print (data.decode(),end='')

print ('')
print ('Total number of characters is:',count)
mysock.close()
