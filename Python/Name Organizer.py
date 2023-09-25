#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU


nameList = input("Please enter your list of names:")

split = nameList.split(";")

for splits in split:
    comma = splits.split(",")
    firstName = comma[1]
    lastName = comma[0]
    print(firstName,lastName)