hours = input('Enter worked hours:')
ihours = float (hours)
rate = input ('Enter pay hourly rate:')
irate = float (rate)
if ihours <= 40 :
    pay = ihours*irate
else :
    pay = (irate*40) + 1.5*(ihours-40)*irate
print ('Gross pay is:', pay)
