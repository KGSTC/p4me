#This code counts the number of times the loop encounters a charachter:
word = input ('Enter string ')
count = 0
for letter in word:
    if letter=='a':
        count =count+1
print (count)
# This code defines a counter function named count:
def count ():
    word = 'Sassaaa'
    count = 0
    for letter in word:
        if letter=='a':
            count =count+1
    print (count)
count ()
 #This code defines and generalises a counter function named count:
def count (string, letter):
     count =0
     for char in string:
         if char== letter:
             count =count+1
     print (count)
count ('bonjour', 'b')
