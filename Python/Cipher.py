#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU


dom = input('Enter a word:')

word = ""

for char in dom:
    offset = ord(char) - ord("a") + 13
    wrap = offset % 26
    newChar = chr(ord("a") +wrap)
    word = word + newChar
print(word)
