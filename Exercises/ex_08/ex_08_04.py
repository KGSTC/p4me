words_in_list =[]
inp=input ('Enter file: ')
handle=open(inp)
#string=handle.read()
#print (string)
for line in handle:
    #print ('This is a line: ', line)
    line.rstrip()
    word_list= line.split()
    #print (word_list)
    for word in word_list:
        if word in words_in_list:
            continue
        else :
            #words_in_list=words_in_list+[word]
            words_in_list.append(word)
orig_words_in_list= words_in_list[:]
words_in_list.sort()
#print ('This is the list of words: \n', orig_words_in_list, '\n', words_in_list)
print (words_in_list)
