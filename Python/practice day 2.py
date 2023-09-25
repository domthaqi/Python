message = "I love Python!"

newMessage = " "

for c in message:
    print(ord(c))
    print(chr(ord(c)+1))
    newMessage = newMessage +chr(ord(c)+1)

print("The coded MSG is:", newMessage)