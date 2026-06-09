# 6. Email Address Validator 
# Problem Statement 
# A user enters an email address: 
# rahul.sharma2026@gmail.com 
# Tasks 
# Write a program to: 
# 1. Extract username.  
# 2. Extract domain name.  
# 3. Extract extension.  
# 4. Count digits present in username.  
# 5. Count special characters.  
# 6. Check whether:  
# o Exactly one '@' exists.  
# o At least one '.' exists after '@'.  
# 7. Display Valid Email or Invalid Email.  
# Sample Output 
# Email: rahul.sharma2026@gmail.com 
 
# Username: rahul.sharma2026 
# Domain: gmail 
# Extension: com 
 
# Digits Found: 4 
# Special Characters Found: 2 
 
# Email Status: Valid

# Input Email Address
email = "rahul.sharma2026@gmail.com"

digit_count = 0
special_count = 0

# Count string attributes
for char in email:
    if char.isdigit():
        digit_count += 1
    elif not char.isalnum() and not char.isspace():
        special_count += 1

# Base initialization for output strings
username = ""
domain = ""
extension = ""
email_status = "Invalid"

# Rule check: Exactly one '@' must exist
if email.count("@") == 1:
    # Break email down manually using .find() boundaries
    at_index = email.find("@")
    username = email[:at_index]
    rest_of_email = email[at_index+1:]
    
    # Rule check: A dot must exist in the domain part after the '@'
    if "." in rest_of_email:
        dot_index = rest_of_email.rfind(".") # Find the last dot index position
        domain = rest_of_email[:dot_index]
        extension = rest_of_email[dot_index+1:]
        email_status = "Valid"

# Display Output
print(f"Email: {email}")
print()
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Extension: {extension}")
print()
print(f"Digits Found: {digit_count}")
print(f"Special Characters Found: {special_count}")
print()
print(f"Email Status: {email_status}")