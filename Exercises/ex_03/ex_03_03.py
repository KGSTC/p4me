print ('Hello')
score = input ('Enter score between 0.0 and 0.1:')
fscore = float (score)
if fscore >= 0.9 and fscore <= 1.0:
    print ('Score grade is A')
elif fscore >=0.8 and fscore <0.9:
    print ('Score grade is B')
elif fscore >=0.7 and fscore <0.8:
    print ('Score grade is C')
elif fscore >=0.6 and fscore <0.7:
    print ('Score grade is D')
elif fscore <0.6:
    print ('Score grade is F')
else:
    print ('Error !')
