#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
dom = input('Enter a csv file: ')
borough = input('Enter borough name: ')
csvFile = input('Enter output csv file: ')
pop = pd.read_csv(dom)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[borough]/pop['count']
pop.plot(x = 'interestdate', y ='Fraction')

mean = pop[dom].mean()
std = pop[dom].std()

print('Max:',pop[dom].max())
print('Min:',pop[dom].min())
print('Mean:',round(mean,3))
print('Standard Deviation:',round(std,3))

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(0)