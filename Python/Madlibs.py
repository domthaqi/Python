#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU



string = "If it VERB like a NOUN and VERB2 like a NOUN, it probably is a NOUN."
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

string.replace("VERB", verb)
string.replace("NOUN", noun)
string.replace("VERB2", verb2)
print("If it", verb , "like a", noun, "and", verb2, "like a", noun+",", "it probably is a", noun+".")