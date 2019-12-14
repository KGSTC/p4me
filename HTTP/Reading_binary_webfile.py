#Reads binary (non-text) web pages, such as images or videos smaller than the size of computer memory:
   ## Open he url
   ##Read in the URL and download all the file contents into a string variable (img)
import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
   ##Write data in a local file
fhand=open('cover3.jpg','wb')#the 'wb' argument opens a binary file for writing only
fhand.write(img)
fhand.close()


#Reads binary (non-text) web pages, such as images or videos of any size and avoids running out of memory(crash, slowing down):
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand=open('cover3.jpg','wb')#the 'wb' argument opens a binary file for writing only
size=0
while True:
    info= img.read(100000)# reads only 100000 characters at a time
    if len(info)<1:break
    size=size+len(info)
    fhand.write(info)# writes characters to the cover3.jpg file
print (size,'characters copied.')
fhand.close()
