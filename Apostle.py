### Simple coding problems


### Python program to swap two variables
## Solution1

x = 5
y = 10

temp = x
x = y
y = temp

print( x,y)

##Solution2

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))

##Solution3

x = 10
y = 50
(x,y) = (y,x)
print("x = ", x, "\n", "y =", y)

##Solution4

a = 9
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)

##Solution5

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x,y = y,x
print("x = ", x,"," " y =", y)

##Solution6

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("x = ", y,"," " y =", x)

##Solution7

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print((x,y) [::-1])

##Solution8

def swap(x,y):
    x,y = y,x
    return x,y

result = swap(2,7)
print(result)

##Solution9

def swap(x,y):
    x,y = y,x
    return(x,y)

x,y = 3,4
print(swap(x,y))

##Solution10

def swap(x,y):
    x,y = y,x
    return (x,y)
x, y = 2, 4
x, y = swap(x,y)
print(x,y) 

##Solution11

x = 10
y = 50

# Swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("Value of x:", x)
print("Value of y:", y) 

##Solution 12

x = 10
y = 50

# Swapping of two variables
# using arithmetic operations
x = x + y
y = x - y
x = x - y

print("Value of x:", x)
print("Value of y:", y) 


###Swap values (elements) in a list

l = [0, 1, 2, 3, 4]
l[0], l[3] = l[3],l[0]
print(l)