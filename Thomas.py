### Simple coding problems
###Sum of all digits in a number:
###Code for Sum of all Digits In Alpha-Numberic String

#1 Without Recursion
string = input("Enter a Alpha-Numeric String: ")
sums = 0
for i in string:
    if( i.isnumeric() ):
        sums = sums+int(i)
print(sums)

@ 
Enter an Alpha-Numeric String: a11s22s55
16
###
#2 Using Recursion

def sumOfNumbers(string, n, sums):
    
    curr_val = string[n]
    if( curr_val.isnumeric() ):
        sums = sums + int(curr_val)
        
    if n == 0:
        return sums
    else:
        return sumOfNumbers(string, n-1, sums)

string = input("Enter a Alpha Numeric String: ")
n = len(string) - 1
print( sumOfNumbers(string, n, sums=0) )

@
Enter an Alpha-Numeric String: study24tonight77
20
###
###Sum of all digits in a number:
# n take it as whole string
n=input("Enter a number: ")
re = 0
for i in n:
    re = re + int(i)
print(re)

n = input("Enter a number:")
sum = 0

for i in range(0, len(n)):
    sum = sum + int(n[i])
print(sum)

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)
###

# Python program to  
# compute sum of digits in   
# number.  
    
# Function to get sum of digits   
def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
    
n = 12345
print(getSum(n))

Output:
15
###
# Python program to  
# compute sum of digits in   
# number.  
    
# Function to get sum of digits   
def getSum(n):  
      
    strr = str(n) 
    list_of_number = list(map(int, strr.strip())) 
    return sum(list_of_number) 
    
n = 12345
print(getSum(n))
Output:
15
###

A. Iterative Approach:
# Python 3 program to  
# compute sum of digits in   
# number.  
    
# Function to get sum of digits   
def getSum(n):  
     
    sum = 0
    while (n != 0):  
        
        sum = sum + (n % 10) 
        n = n//10
        
    return sum
    
n = 12345
print(getSum(n))

Output:
15

###

B. Recursive Approach:
Python3
# Python program to compute  
# sum of digits in number.  
    
def sumDigits(no):  
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))   
    
# Driver code  
n = 12345
print(sumDigits(n))
Output:
15

###
# Python program to sum all the digits of an input number

num = int(input("Enter a Number: "))
result = 0
hold = num

# while loop to iterate through all the digits of input number
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

# displaying output
print("Sum of all digits of", hold, "is: ", result)
Output 1:
Enter a Number: 5257
Sum of all digits of 5257 is:  19

###
using While Loop

# Python Program to find Sum of Digits of a Number using While Loop

Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("Sum of the digits %d is: %d" %(Number,Sum))



###

Using Functions
# Python Program to find Sum of Digits of a Number using Functions

def Sum_Of_Digits(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("Sum of the digits %d is: %d" %(Number,Sum))

###
using Recursion:
# Python Program to find Sum of Digits of a Number using Recursion

Sum = 0
def Sum_Of_Digits(Number):
    global Sum
    if(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Sum_Of_Digits(Number //10)
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("Sum of the digits %d is: %d" %(Number,Sum))

###
#
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
print(sum_digits(123))

###
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
print(sum_digits3(123))

###

###generate a random number:

import random
n = random.randint(2, 10)
print(n)

##
import random
print(random.random())

### 

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

