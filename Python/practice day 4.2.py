workdays = "Monday?Tuesday?Wednesday?Thursday?"
summerMonths = "*June*July*August*"
longWeekend = "Friday_Saturday_Sunday"
seasons = "+Spring+Summer+Fall+Winter"

print(summerMonths[1:5],workdays[25:33]) # prints June Thursday

months = summerMonths[:].split("*")
print('Summer has', len(months),"months")


numbers = "10 / 11 / 12 / 13 / 14"
numList = numbers.split(" / ")
for n in numList:
    print(n)

