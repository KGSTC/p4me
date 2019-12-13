#This code repeatedly prompts a user for integer numbers until the user enters 'done'. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Once 'done' is entered, print out the largest and smallest of the numbers.

    ##This code is to store  user input in list in python
list =[]
    ### This loop prompts for user input and breaks when user is done:
while True:
    x= input ('Please enter an integer or enter done:')
    if x=='done':
        break
    ####This Try/Except code is to catch non integer entries:
    try:
        ix=float(x)
        ##This code is to store  user input in list in python
        list.append(ix)
    ####This Try/Except code is to catch non integer entries:
    except:
        print ('Invalid input')
        ##!! We could add a line in Except code : continue ==> to go back to the loop, but without continue the code is doing all right here
print (list)
#This code calculates sum, average, smallest, greatest value in a list:
sum_values = 0
counter_variable=0
average=0
smallest_variable = None
largest_so_far = None
for value in list:
    ##For Sums:
    sum_values= sum_values + value
    ##For average
    counter_variable= counter_variable+1
    average= sum_values / counter_variable
    ##For smallest value in a list
    if smallest_variable is None:
        smallest_variable=value
    if value<smallest_variable:
        smallest_variable =value
    ##For largest value in a list
    if largest_so_far is None:
        largest_so_far= value
    if value > largest_so_far:
        largest_so_far = value
print ('Sum is:', sum_values)
print('Average is', average)
print ('Maximum is:', largest_so_far)
print ('Minimum is:', smallest_variable)
