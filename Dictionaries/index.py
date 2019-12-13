##This code reads in a file(1 word/1 line), creates a new key for every new first letter and matches each word to the first letter:
inp=input('Enter file: ')
handle=open (inp)
words = {}
for line in handle:
    line = line.strip()
    first = line[0]
    if first not in words:
        words[first] = []
    words[first].append(line)
print (words)
#This code creates a new dictionary using 'defaultdict' from 'collections' module and adds words by first letter:
## better code if use of collections is not limited
import collections
words = collections.defaultdict(list)# creates an empty dictionary
with open('index.txt') as f:
    lines = [l.strip() for l in f if l.strip()]
#print(lines)# List of words
for word in lines:
    words[word[0]].append(word)
print (words)
#outputs: defaultdict(<type 'list'>, {'a': ['airport'], 'b': ['bathroom', 'boss', 'bottle'], 'e': ['elephant']})
