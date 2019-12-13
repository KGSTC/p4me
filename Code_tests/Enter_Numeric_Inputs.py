#Data is read in strings. Then, data is parsed and converted as needed.
#=> control over error situations/error inputs
# raw input numbers must be converted from strings
var = input ('Please enter a number:')
try:
    fvar = float (var)
    print (fvar)
except:
    print ('Invalid input')
