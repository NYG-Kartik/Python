# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/28/23
# This program works with a CSV file

# import libraries
import matplotlib.pyplot as plt
import pandas as pd

# read the csv file
df = pd.read_csv('workforce.csv')

# print average of applied for the program in each borough
average = df.groupby('Borough')['Applied for the program'].mean()
print(average)
grouped_data = df.groupby('Borough')
# print possible boroughs and choose from it
print('The possible boroughs to choose from:', df.groupby('Borough').groups.keys())

# input from user
choice = input('Enter a borough:')

# get the data from the chosen borough and store in variable chosenBorough
chosenBorough = df.groupby('Borough').get_group(choice)

# max applicants, min applicants
max_applicants = chosenBorough['Applied for the program'].max()
min_applicants = chosenBorough['Applied for the program'].min()
years = len(chosenBorough['Year'].unique())

# print these values
print("the maximum number of applicants that applied for the program:", max_applicants)
print("the minimum number of applicants that applied for the program:", min_applicants)
print("the number of available year records in the borough are", years)

# specify output file from user
y = input('Enter output file name:')


grouped_data.get_group(choice).plot.bar(x='Year' , y='Applied for the program')
 

plt.xlabel("Year")
plt.ylabel("Applied for the program")
plt.gcf().subplots_adjust(bottom=0.25)


plt.savefig(y)


