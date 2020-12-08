### Simple coding problems
###Convert Celsius to Fahrenheit:

c = float(input("Enter temperature in Celsius: "))
f = ((c * 9)/ 5 + 32)
print("Temperature from celsius to fahrenheit is: ", f)

###

def far(c):
    f = ((c * 9) / 5 + 32)
    return f

z = far(30)
print(z)
@ 86.0


###

def far(c):
    f = ((c * 9) / 5 + 32)
    print(f)
    return

far(30)

@ 86.0
###

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

###
###Prime number or not

n = int(input("Enter the number: "))
if n >1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime.")
            print(i, "times", n//i, "is", n)
            break
    else:
        print("Prime.")
else:
    print("Not Prime.")

###

###Remove duplicate from a list

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

### in function

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)


