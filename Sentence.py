#Kartik Vanjani
#KARTIK.VANJANI21@myhunter.cuny.edu
#2/10/23
# This program reverses a string separated by commas, and 
# prints them normally, upper case, and lower case.
sentence = input('Enter three words separated by comma (,):')
bros = sentence.split(',')
bros.reverse()
sis = " ".join(bros)
print("new string:", sis)
print("lower case:", sis.lower())
print("upper case:", sis.upper())