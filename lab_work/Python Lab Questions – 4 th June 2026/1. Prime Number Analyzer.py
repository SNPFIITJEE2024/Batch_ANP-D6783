#Problem Statement: Accept a number from the user and determine whether it is a prime number or not. Additional Requirement: If the number is not prime, display all its factors.

# Accept an integer input from the user
num = int(input("Enter a number: "))

# A list to store the factors of the number
factors = []

# Loop from 1 up to the number itself to find all factors
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)  # Add the divisor to the factors list

# A prime number has exactly 2 factors (1 and itself) and must be greater than 1
if len(factors) == 2 and num > 1:
    print(f"{num} is a Prime Number")
else:
    # If it's not prime, display the list of factors collected
    print("Factors:", *factors)
    print(f"{num} is not a Prime Number")