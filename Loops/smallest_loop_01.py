smallest_variable = None
for x in [12,90,3545,9,445,3,987,98,2,374,0,9787,90]:
    if smallest_variable is None:
        smallest_variable=x
    if x<smallest_variable:
        smallest_variable =x 
    print ('The smallest number so far is:', smallest_variable)
print ('The smallest variable in the set is:', smallest_variable)
