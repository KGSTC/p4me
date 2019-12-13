largest_so_far = None
for x in [3,41,12,9,74,15]:
    if largest_so_far is None:
        largest_so_far= x
    if x > largest_so_far:
        largest_so_far = x
    print ('The largest number so far is:', largest_so_far)
print ('The largest number is:', largest_so_far)
