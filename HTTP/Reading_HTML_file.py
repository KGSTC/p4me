#Reading a html web page : Web scraping
import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://wwww.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
