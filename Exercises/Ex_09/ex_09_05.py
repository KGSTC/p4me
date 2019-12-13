#This code reads in a file, finds a line starting with specific criteria,splits it to return the right end of the line(string):
inp=input ('Enter file name: ')
try:
    h=open (inp)
except:
    print('Invalid input !')
    exit()
domains_list=[]
for line in h:
    line=line.rstrip()
    #words=line.split()
    if line.startswith ('From:'):
        #print (line)
        #delimiter='@'
        t=line.split('@')## uname,domain = line.split('@')
        #print (t[1])
        domains_list.append (t[1])
#print (domains_list)
d={}
for domain in domains_list:
    d [domain]=d.get (domain,0)+1
print (d)
#Another option would be:
inp=input ('Enter file name: ')
try:
    h=open (inp)
except:
    print('Invalid input !')
    exit()
d={}
for line in h:
    line=line.rstrip()
    #words=line.split()
    if line.startswith ('From:'):
        #print (line)
        #delimiter='@'
        uname,domain = line.split('@')##creates a tuple (uname,domain)
        #print ((uname,'***',domain))
        d [domain]=d.get (domain,0)+1
print (d)
