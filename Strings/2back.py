# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 2/14/23
# This program prints the ASCII code of the input string, and 
# the letter two letters back of each letter in the inputed string
x = input("Enter a phrase:")  
print("letter ASCII two_letter_before")
for i in x:   
    print("%6c %5i %17c"%(i, ord(i), chr(ord(i)-2)))
