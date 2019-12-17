# Parse HTML and extracts substrings that match a particular pattern: prompts for a web adress, opens the web page, reads the data and passes the data to the BeautifulSoup parser and then retrieves all of the tags and prints out the href attribute for each tag:
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup #Import BeautifulSoup library to extract data from even broken HTML input
import ssl

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
    print (tag.get('href',None))
