# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/30/23
# This program extracts the first and last name from an email
def main():
    x = input('Enter an email:')
    y = x.split('@')
    z = str(y[0])
    z1 = z.split('20')
    z2 = str(z1[0])
    z3 = z2.split('.')
    print('first name:', z3[0])
    print('last name:', z3[1])
   
if __name__ == "__main__":
    main()
