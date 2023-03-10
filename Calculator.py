# Kartik Vanjani
# This is my PYTHON Calculator that adds, subtracts, divides, or multiplies two numbers
print('Welcome to Kartiks Calculator!')
print('(a) add')
print('(b) subtract')
print('(c) multiply')
print('(d) divide')
choice = input('Which operation would you like to perform?')
if choice == "a":
    cool = float(input('Enter your first value to add:'))
    cool2 = float(input('Enter your second value to add:'))
    print("Your answer is", cool + cool2)
elif choice == "b":
    nice = float(input('Enter your first value to subtract:'))
    nice2 = float(input('Enter your second value to subtract:'))
    print("Your answer is", nice - nice2)
elif choice == "c":
    yo = float(input('Enter your first value to multiply:'))
    yo2 = float(input('Enter your second value to multiply:'))
    print("Your answer is", yo*yo2)
elif choice == "d":
    bro = float(input('Enter the dividend:'))
    bro2 = float(input('Enter your divisor:'))
    print('Your answer is', bro/bro2)
else:
    print('Invalid choice, choose only a, b c, or d')
