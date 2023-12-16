# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 2/19/23
# This program: prompts the user to enter a word and then prints out the word with each letter 
# shifted right by 13
x = input('Enter an all-big-letter string:')
y = int(input('Enter a non-negative int to shift:'))
codedWord = ""
for ch in x:
    codedWord = codedWord + chr((ord(ch) + y -65 ) % 26 +65)

print('ciphered string:', codedWord)
