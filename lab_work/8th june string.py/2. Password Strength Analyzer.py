# 2. Password Strength Analyzer 
# Problem Statement 
# A user enters a password. 
# Python@2026! 
# Tasks 
# Write a program to determine whether the password is Strong, Medium, or Weak. 
# Rules: 
# • Minimum length 8  
# • Contains at least:  
# o 1 uppercase letter  
# o 1 lowercase letter  
# o 1 digit  
# o 1 special character  
# Additionally: 
# 1. Count uppercase letters.  
# 2. Count lowercase letters.  
# 3. Count digits.  
# 4. Count special characters.  
# 5. Display all digits separately.  
# 6. Display all special characters separately.  
# Sample Output 
# Password: Python@2026! 
 
# Uppercase Letters: 1 
# Lowercase Letters: 5 
# Digits: 4 
# Special Characters: 2 
 
# Digits Found: ['2', '0', '2', '6'] 
# Special Characters Found: ['@', '!'] 
 
# Password Strength: Strong 

# Input Password
password = "Python@2026!"

# Set up tracking variables
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digits_found = []
special_found = []

# Define standard special characters to check against
special_chars_string = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~"

# Scan the password
for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
        digits_found.append(char)
    elif char in special_chars_string:
        special_count += 1
        special_found.append(char)

# Check criteria rules
has_min_length = len(password) >= 8
has_upper = upper_count >= 1
has_lower = lower_count >= 1
has_digit = digit_count >= 1
has_special = special_count >= 1

# Calculate how many individual type rules passed
conditions_passed = sum([has_upper, has_lower, has_digit, has_special])

if has_min_length and conditions_passed == 4:
    password_strength = "Strong"
elif has_min_length and conditions_passed >= 2:
    password_strength = "Medium"
else:
    password_strength = "Weak"

# Display Output
print(f"Password: {password}")
print()
print(f"Uppercase Letters: {upper_count}")
print(f"Lowercase Letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_count}")
print()
print(f"Digits Found: {digits_found}")
print(f"Special Characters Found: {special_found}")
print()
print(f"Password Strength: {password_strength}")