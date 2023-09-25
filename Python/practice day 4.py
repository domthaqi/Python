names = ["amy", "roger", "amber", "mandy","diana","aida"]
for i in range(1,6,2):
    print(names[i], end= ' ') # prints roger mandy aida

quote = ' "My life is my message." -- Mahatma Gandhi'
print(quote[29:44]) #Prints Mahatma Gandhi
print(quote[2:4].lower()) #prints my
print("This quote has",end= " ")
print(quote.count('.'), "period") #prints count of periods in quote

