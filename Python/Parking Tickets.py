#Import pandas for reading and analyzing CSV data:
import pandas as pd

fileName = input("Enter file name:")
attribute = input("Enter attritube:")

tickets = pd.read_csv(fileName)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe