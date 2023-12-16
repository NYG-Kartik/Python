# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/9/23
# This program converts gallons to liters and vice versa

print('(a) convert gallon to liter')
print('(b) convert liter to gallon')
x = input('Enter a or b:')
if x == "a":
    y = float(input('Enter number of gallons:'))
    liters = y * 3.79
    print(y, "gallons =", round(liters,2), "liters")
elif x == "b":
    z = float(input('Enter number of liters:'))
    gallons = z * 0.26
    
    print(z, "liters =", round(gallons,2), "gallons")
else:
    print('Wrong choice, please enter only a or b')

