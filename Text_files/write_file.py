#This code writes in a file
file_name=input ('Please, enter file name: ')
fout = open (file_name, 'w')
print (fout)
line1= 'This is the list of our family members: \n'
fout.write (line1)
line2= 'Anawr\n'
fout.write (line2)
line3='Kaouther\n'
fout.write (line3)
line4='Hamid\n'
fout.write (line4)
line5='Alhamdullilah\n'
fout.write (line5)
fout.close()##Closing the file==> Saves data in the disc
