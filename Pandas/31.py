# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/27/23
# This program works with a CSV file
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('workforce.csv')

df['Acceptance rate'] = (df["Were placed into full-time or part-time jobs"] / df["Applied for the program"]) * 100

year = int(input('Enter a year from 2017 to 2021:'))

chosenYear = df.groupby('Year').get_group(year)

maxIdx = chosenYear['Acceptance rate'].idxmax()
maxBorough = chosenYear["Borough"][maxIdx]
maxRate = chosenYear['Acceptance rate'][maxIdx]

print(round(maxRate, 2))
print(maxBorough)


#TODO: prompt to enter output file name.
output = input('Enter output file name:')
#TODO: plot acceptance rate by different boroughs
#in that GIVEN year.

plt.plot(chosenYear['Borough'], chosenYear['Acceptance rate'])

chosenYear.plot(x = "Borough", y = "Acceptance rate")

#TODO: save the plot in the given output file.

fig = plt.gcf()
plt.savefig(output)


