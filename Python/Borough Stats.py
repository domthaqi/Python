#DAMENIK THAQI
#DAMENIK.THAQI50@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd
dom = input("Enter borough name:")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
pop.plot(x="Year")

print("Average Population:", pop[dom].mean())
print("Max Population:", pop[dom].max())
      