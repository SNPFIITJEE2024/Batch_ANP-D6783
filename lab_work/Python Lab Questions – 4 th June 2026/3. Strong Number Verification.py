#Problem Statement: A Strong Number is a number whose sum of factorials of digits equals the number itself. Write a program to check whether a given number is a Strong Number. Example: Input: 145 Output: 145 is a Strong Number

# Accept an integer input from the user
num = int(input("Enter a number: "))

# Keep a backup of the original number for the final comparison
temp = num
sum_of_factorials = 0

# Loop until all digits are processed
while temp > 0:
    # Extract the last digit of the number
    digit = temp % 10
    
    # Calculate the factorial of the extracted digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
        
    # Add the calculated factorial to our running total sum
    sum_of_factorials += factorial
    
    # Remove the last digit from temp to move to the next digit
    temp //= 10

# Check if the total sum of factorials matches the original number
if sum_of_factorials == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")