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
