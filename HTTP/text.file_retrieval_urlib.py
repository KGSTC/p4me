#Retrieve a web file using the library 'urllib'
import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')# Opens the file handle and takes out the header
for line in fhand:
    print (line.decode().strip())
#Retrieves and counts words in a text document from web server:
import urllib.request, urllib.parse, urllib.error
counts=dict()
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print (counts)
