# Parse HTML and extracts substrings that match a particular pattern: prompts for a web adress, opens the web page, reads the data and passes the data to the BeautifulSoup parser and then retrieves all of the tags and prints out the href attribute for each tag:
## Gets all HTML anchor tags including relative paths (e.g., tutorial/index.html) or in-page references (e.g., '#') that might not include "http[s]://"
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup #Import BeautifulSoup library to extract data from even broken HTML input
import ssl                     # BeautifulSoup can be installed in your computer (using Anaconda3 for Python3.6 and further) or download the file bs4 (http://www.pye.com/code3/bs4.zip and unzip it in the same directory as this file)

# Ignores ssl certificate errors:
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input ('Enter - ')
html= urllib.request.urlopen(url,context=ctx).read()#context=ctx<=>
soup=BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags and prints out the href attribute for each tag:
tags=soup('a')
for tag in tags:
        #Look at different parts of a tag (TAG, URL, Contents, Attrs)
    print ('TAG:', tag)
    print ('URL:', tag.get('href',None))
    print ('Contents:', tag.contents[0])
    print ('Attrs:', tag.attrs)
