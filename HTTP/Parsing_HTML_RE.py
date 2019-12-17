#Parses HTML web pages to repeatedly search for substrings using RE:
import urllib.request, urllib.parse, urllib.error
import re
import ssl #allows this program to access websites that strictly enforce HTTPS.

#Ignores SSL certficate errors:
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#Reads file and extract matchin expressions:
url =input ('Enter - ')
html=urllib.request.urlopen(url).read() #read() method returns HTML source code as a bytes object
links= re.findall (b'href="(http[s]?://.*?)"',html)# b' bla bla'<=> decode(), as data is received in utf code and not a string #http[s]: http or https # ?: don't be greedy: exactly matching #
for link in links:
        print (link.decode().rstrip())
print ('End of task 1')
print ('')


#For line in hand:
    #line = line.rstrip()
    #x= re.findall('\S+@\S+',line) # \S+ : one or more non-blank character. + applies to the immediate on the left character
    #if len(x)>0: # if list is not empty print list
        #print (x)
#print ('End of task 3')
#print ('')
