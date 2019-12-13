sum_variable = 0
counter_variable = 0
for x in [1,2,0,3,0,6]:
    counter_variable=counter_variable+1
    sum_variable = sum_variable +x
    average = sum_variable / counter_variable
    print (counter_variable,sum_variable, average)
print('The average in this set is:', average)
