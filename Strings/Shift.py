sen = input("Enter an all-big-letter string:")
x = input("Enter a non-negative int to shift:")
for c in sen:
    print(chr(ord(c)+13))