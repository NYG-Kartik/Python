# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/21/23
# This program works with a CSV file
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('demo_boro.csv')
x = input('Enter borough name:')
y = input('Enter output file name')

df['Grade K-6 Enrollment Fraction'] = (df['Grade K'] + df['Grade 1'] + df['Grade 2'] + 
df['Grade 3'] + df['Grade 4'] + df['Grade 5'] + df['Grade 6']) / (df['Total Enrollment'] )


pop = df.query("Borough=='"+ x + "'")

print('minimum of total enrollment for', x, 'is', pop["Total Enrollment"].min())
print('maximum of total enrollment for', x, 'is', pop["Total Enrollment"].max())
print('median of total enrollment for', x, 'is', pop["Total Enrollment"].median())
print('mean of total enrollment for', x, 'is', pop["Total Enrollment"].mean())
print('stand deviation of total enrollment for', x, 'is', round(pop["Total Enrollment"].std(), 3))

pop.plot(x="Year", y="Grade K-6 Enrollment Fraction")

plt.savefig(y)
