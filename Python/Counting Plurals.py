#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU


nouns = input("Enter nouns: ")

empty = " "
count = 0

list = nouns.split(empty)

numberOfElements = len(list)
print("Number of words:", numberOfElements)

for word in list:
    if word.endswith("s"):
        count += 1

pluralFraction = count/numberOfElements
print("Fraction of your list that is plural:", pluralFraction)