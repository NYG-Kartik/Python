# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 4/3/23
# This program prints stuff from data using a function

def rentPrice(borough, roomType):
    if borough == "Manhattan":
        if roomType == "studio":
            return 2795
        elif roomType == "1-bedroom":
            return 3500
        elif roomType == "2-bedroom":
            return 3900
        else:
            return 0
    elif borough == "Brooklyn":
        if roomType == "studio":
            return 2273
        elif roomType == "1-bedroom":
            return 2450
        elif roomType == "2-bedroom":
            return 2750
        else:
            return 0
    elif borough == "Queens":
        if roomType == "studio":
            return 1695
        elif roomType == "1-bedroom":
            return 1900
        elif roomType == "2-bedroom":
            return 2350
        else:
            return 0
    elif borough == "Bronx":
        if roomType == "studio":
            return 1500
        elif roomType == "1-bedroom":
            return 1700
        elif roomType == "2-bedroom":
            return 2200
        else:
            return 0
    elif borough == "Staten Island":
        if roomType == "studio":
            return 1200
        elif roomType == "1-bedroom":
            return 1425
        elif roomType == "2-bedroom":
            return 2000
        else:
            return 0
    else:
        return 0