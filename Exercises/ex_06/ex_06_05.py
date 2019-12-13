text = 'X-DSPAM-Confidence:    0.8475'
str= text.find (':')
print (float (text[str+5:]))
