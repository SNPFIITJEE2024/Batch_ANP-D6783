# 1. Employee ID Validation and Analysis System 
# Problem Statement 
# A company generates employee IDs in the following format: 
# EMP2026ANUJ458 
# Tasks 
# Write a program to: 
# 1. Count the number of uppercase letters.  
# 2. Count the number of digits.  
# 3. Extract the joining year.  
# 4. Extract the employee name.  
# 5. Check whether the ID follows these rules:  
# o Starts with "EMP"  
# o Contains exactly 4 digits for the year  
# o Ends with exactly 3 digits  
# 6. Create a list containing all digits present in the ID.  
# 7. Find the sum of all digits present in the ID.  
# 8. Display whether the ID is valid or invalid.  
# Sample Output 
# Employee ID: EMP2026ANUJ458 
 
# Uppercase Letters: 7 
# Digits: 7 
 
# Joining Year: 2026 
# Employee Name: ANUJ 
 
# Digit List: [2, 0, 2, 6, 4, 5, 8] 
# Sum of Digits: 27 
 
# ID Status: Valid

# Input Employee ID
emp_id = "EMP2026ANUJ458"

# Initialize normal tracking variables
uppercase_count = 0
digit_count = 0
digit_list = []

# Loop through character by character
for char in emp_id:
    if char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
        digit_list.append(int(char)) # Convert to number and add to list

# Calculate sum of digits
digit_sum = sum(digit_list)

# Extract Year and Name using string slicing indices
joining_year = emp_id[3:7]
emp_name = emp_id[7:-3] # Everything between year and last 3 digits

# Rule Validation Check
starts_with_emp = emp_id.startswith("EMP")
year_is_numeric = joining_year.isdigit() and len(joining_year) == 4
last_three_digits = emp_id[-3:].isdigit() and len(emp_id[-3:]) == 3

if starts_with_emp and year_is_numeric and last_three_digits:
    id_status = "Valid"
else:
    id_status = "Invalid"

# Display Output
print(f"Employee ID: {emp_id}")
print()
print(f"Uppercase Letters: {uppercase_count}")
print(f"Digits: {digit_count}")
print()
print(f"Joining Year: {joining_year}")
print(f"Employee Name: {emp_name}")
print()
print(f"Digit List: {digit_list}")
print(f"Sum of Digits: {digit_sum}")
print()
print(f"ID Status: {id_status}")