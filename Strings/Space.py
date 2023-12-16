# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/16/23
# This program prints the contents of a sentence seperated by spaces

a = input('Enter a list of words, separated by a space:')
y = list(a.split(' '))
z = len(y)
count = 0
for i in range(z-1):
    if y[i][0] == "a":
        count = count + 1
    if y[i][0] == "b":
        count = count + 1
percent = count / z
print('number of words:', z)
print('number of words starting with a or b:', count)
print('fraction of words starting with a or b', round(percent, 2))
