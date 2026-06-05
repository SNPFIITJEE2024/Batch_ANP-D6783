#Problem Statement: Accept a number from the user. Display: • Reverse Number • Whether it is a Palindrome Example: Input: 1221 Output: Reverse: 1221 Palindrome Number
# --- Step 1: Take input from the user ---
num = int(input("Enter a number: "))

# Keep a backup of the original number for comparison later
original_num = num
reverse_num = 0

# --- Step 2: Reverse the number using math ---
while num > 0:
    # Extract the last digit of the number
    remainder = num % 10
    
    # Push the existing reversed number over by one decimal place and add the digit
    reverse_num = (reverse_num * 10) + remainder
    
    # Drop the last digit from the original number
    num //= 10

# --- Step 3: Print results and check for Palindrome ---
print(f"Reverse: {reverse_num}")

if original_num == reverse_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")