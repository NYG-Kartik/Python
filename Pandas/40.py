# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 4/18/23
# This program works with CSV files 
import pandas as pd

csvFile = "restaurant_inspection.csv"

df = pd.read_csv(csvFile)

num1 = int(input('order of most common violation:'))

print(df["VIOLATION DESCRIPTION"].value_counts()[:num1])

num2 = int(input('order of most popular cuisine description'))

print(df["CUISINE DESCRIPTION"].value_counts()[:num2])