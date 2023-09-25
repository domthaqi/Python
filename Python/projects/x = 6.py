x = 6
y = x % 4 #2
w = y ** 2
z = w // 2
print(y)
print(w)
print(z)

print(x,y,w,z)
x,y = y,w
print(x,y,w,z)
x = y / 2
print(x,y,w,z)
