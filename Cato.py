### nested pattern

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



### Fibonacci series by for loop

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



### Fibonacci series by while loop

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

