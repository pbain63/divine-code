### Program: nested_pattern.py

# Initialize the first five rows
n = 5

# Start the loop to print the first five rows
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Start the loop to print the remaining rows in decreasing order of stars
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')    



###Program: Fibonacci series by for loop

# Initialize `first_no` to `0`
first_no = 0

# Initialize `second_no` to `1`
second_no = 1

# Initialize `numbers`
numbers = range(0, 11)

# Find and display Fibonacci series
for num in numbers:
    if (num <= 1):
        # Update only `nth`
        nth = num
    else:
        # Update the values `nth`, `first_no` and `second_no`
        nth = first_no + second_no
        first_no = second_no
        second_no = nth

    # Print `nth`
    print(nth)



###Program: Fibonacci series by while loop

# Set `fib_no` to 55, the number until where you want to print
fib_no = 55

# Set `first_no` to 0
first_no = 0

# Set `second_no` to 1
second_no = 1

# Set the counter `count` to 0
count = 0

# while loop to print the fibonacci series until the `fib_no`
while first_no <= fib_no:
    # Print `first_no`
    print(first_no)

    # Fibonnacci number
    nth = first_no + second_no

    # update values of `first_no` and `second_no`
    first_no = second_no
    second_no = nth

    # Set counter `count` +1
    count += 1


###Program: Recursion 

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


###Program: A simple guess game by while 

import random
upper_bound = 20
lower_bound = 1
adaptive_upper_bound = upper_bound
adaptive_lower_bound = lower_bound
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("Guess new number: "))
    if guess <= 0:
        print("Sorry, you're giving up.")
        break
    if guess < lower_bound or guess > upper_bound:
        print("Guess not within boundaries!")
    elif guess < adaptive_lower_bound or guess > adaptive_upper_bound:
        print("Your guess is contradictory to your previous guess!")
    elif guess > to_be_guessed:
        adaptive_upper_bound = guess - 1
        print("Number is too high!")
    elif guess < to_be_guessed:
        adaptive_lower_bound = guess + 1
        print("Number is too small!")

else:
    print("Congratulations! You made it!")

###
### #Program: Declare global variable name for use in all functions
name = str(input('Enter your name: '))


# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


# Iterate over letters in name string
def print_letters():
    for letter in name:
        print(letter)


# Define main method that calls other functions
def main():
    has_vowel()
    print_letters()


# Execute main() function
if __name__ == '__main__':
    main()

##

###Program: Fibonacci boundaries: the largest fibonacci
    #number smaller than x and the lowest
    #fibonacci number higher than x

def fib_intervall(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    (old, new) = (0, 1)
    while True:
        if new < x:
            (old, new) = (new, old + new)
        else:
            if new == x:
                new = old + new
            return (old, new)


while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))



##
