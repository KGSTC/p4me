#Parses HTML web pages to repeatedly search for substrings using RE:
import urllib.request, urllib.parse, urllib.error
import ssl #allows this program to access websites that strictly enforce HTTPS.

#Ignores SSL certficate errors:
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#Reads file and extract matchin expressions:
url =input ('Enter URL - ')
#Checks the validity of url provided by user
try:
    html=urllib.request.urlopen(url)
except:
    print ('Enter valid URL:')
    exit()
count = 0
for line in html:
    text=line.decode().rstrip()
    count+= len(text)
    if count <= 3000:
        print (text)

print ('Count-', count)
