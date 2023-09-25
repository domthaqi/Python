#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter input file: ")
outputFile = input("Enter output file: ")

homeless = pd.read_csv(inputFile)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = 'Fraction Children')

dom = plt.gcf()
dom.savefig(outputFile)