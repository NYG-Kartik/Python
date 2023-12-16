# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/31/23
# This program prints thee website name

def main():

    x = input('input a website:')
    y = x.split('.')
    if len(y) == 3:
        print('website name:', y[1])
    else:
        print('website name:', y[0])

    if y[len(y) - 1] == "com":
        print('commercial')
    elif y[len(y) - 1] == "edu":
        print('education')
    elif y[len(y) - 1] == "org":
        print('organization')
    elif y[len(y) - 1] == "gov":
        print('government')
    else:
        print('other')

if __name__ == "__main__":  
    main()