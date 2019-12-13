hours = input ('Enter worked hours:')
rate = input ('Enter rate par hour:')
h = float (hours)
r = float (rate)
def computepay (h,r):
    if h <= 40 :
        pay = h*r
    else :
        pay = (r*40) + 1.5*(h-40)*r
    return pay
pay = computepay (h,r)
print (pay)
