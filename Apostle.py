### Simple coding problems


### Python program to swap two variables


x = 5
y = 10

temp = x
x = y
y = temp

print( x,y)
'''
'''
a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
'''
"""
x = 10
y = 50
(x,y) = (y,x)
print("x = ", x, "\n", "y =", y)
"""
'''
a = 9
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)
'''
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x,y = y,x
print("x = ", x,"," " y =", y)
'''
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("x = ", y,"," " y =", x)
'''
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print((x,y) [::-1])'''
'''
def swap(x,y):
    x,y = y,x
    return x,y

result = swap(2,7)
print(result)'''
'''
def swap(x,y):
    x,y = y,x
    return(x,y)

x,y = 3,4
print(swap(x,y))'''
'''
def swap(x,y):
    x,y = y,x
    return (x,y)
x, y = 2, 4
x, y = swap(x,y)
print(x,y) '''
'''
x = 10
y = 50

# Swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("Value of x:", x)
print("Value of y:", y) '''
'''
x = 10
y = 50

# Swapping of two variables
# using arithmetic operations
x = x + y
y = x - y
x = x - y

print("Value of x:", x)
print("Value of y:", y) '''
##Swap values (elements) in a list
l = [0, 1, 2, 3, 4]
l[0], l[3] = l[3],l[0]
print(l)