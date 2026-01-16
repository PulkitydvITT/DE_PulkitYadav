x = 10
y = 20

#One way : 
x , y = y , x 
print(x)
print(y)

#Another way : 
x = x + y
y = x - y
x = x - y
print()
print(x)
print(y)