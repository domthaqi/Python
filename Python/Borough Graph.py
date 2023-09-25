#DAMENIK THAQI
#DAMENIK.THAQI50@myhunter.cuny.edu

import pandas as pd 
import matplotlib.pyplot as plt

population = pd.read_csv('nycHistPop.csv',skiprows=5)
population['Fraction'] = population[input('Enter Borough')]/population['Total']

population.plot(x = 'Year', y = 'Fraction')

dom = plt.gcf()
dom.savefig(input("Enter output file name:"))