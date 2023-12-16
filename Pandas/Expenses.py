# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/22/23
# This program deals with CSV files regarding expenses

#Import libraries
import matplotlib.pyplot as plt
import pandas as pd

#Read the csv file
pop = pd.read_csv('expenses.csv')

# Print the choices
print('a. group by category')
print('b. group by year-month')
print('c. most visited stores')
# User choice
choice = input('Enter a choice:')

if choice == "a":
    groupedData = pop.groupby('Category')
    print(pop.groupby('Category')['Amount'].sum())
    print('All Possible Categories:', groupedData.groups.keys())
    x = input('Enter a specific category, calculate its minimum, maximum, average, and total amount for that category')
    min = pop.groupby('Category')['Amount'].get_group(x).min()
    max = pop.groupby('Category')['Amount'].get_group(x).max()
    avg = pop.groupby('Category')['Amount'].get_group(x).mean()
    sum = pop.groupby('Category')['Amount'].get_group(x).sum()
    print('min:', round(min, 2))
    print('max:', round(max, 2))
    print('average:', round(avg, 2))
    print('total:', round(sum, 2))
if choice == "b":
    pop['Year Month'] = pd.to_datetime(pop['Date']).dt.strftime('%Y-%m')
    groupedData2 = pop.groupby('Year Month')
    print(pop.groupby('Year Month')['Amount'].sum())
    print('Available Categories:',groupedData2.groups.keys())
    y = input('Enter a year-month, calculate its minimum, maximum, average, and total amount for that month')
    print('min:', round(pop.groupby('Year Month')['Amount'].get_group(y).min(), 2))
    print('maximum:', round(pop.groupby('Year Month')['Amount'].get_group(y).max(), 2))
    print('average:', round(pop.groupby('Year Month')['Amount'].get_group(y).mean(), 2))
    print('sum:', round(pop.groupby('Year Month')['Amount'].get_group(y).sum(), 2))
    
if choice == "c":
    groupedData3 = pop.groupby('Store')
    z = int(input('Enter an integer'))
    woah = pop['Store'].value_counts().nlargest(z)
    print('The first many most visited stores', woah)
else:
    print('wrong choice')

    
   
