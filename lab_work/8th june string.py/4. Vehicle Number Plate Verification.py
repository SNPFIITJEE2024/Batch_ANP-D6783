# 4. Vehicle Number Plate Verification 
# Problem Statement 
# A vehicle number plate is entered: 
# MH12AB4589 
# Tasks 
# Write a program to: 
# 1. Extract state code.  
# 2. Extract district code.  
# 3. Extract vehicle series.  
# 4. Extract vehicle number.  
# 5. Count letters and digits separately.  
# 6. Verify:  
# o First 2 characters must be alphabets.  
# o Next 2 must be digits.  
# o Next 2 must be alphabets.  
# o Last 4 must be digits.  
# 7. Display whether the number plate is valid.  
# Sample Output 
# Vehicle Number: MH12AB4589 
# State Code: MH 
# District Code: 12 
# Series: AB 
# Vehicle Number: 4589 
 
# Total Letters: 4 
# Total Digits: 6 
 
# Vehicle Number Status: Valid

# Input Vehicle Number Plate
plate_number = "MH12AB4589"

total_letters = 0
total_digits = 0

# Count letters and digits across string
for char in plate_number:
    if char.isalpha():
        total_letters += 1
    elif char.isdigit():
        total_digits += 1

# Extract plate blocks via static slicing indices
state_code = plate_number[0:2]
district_code = plate_number[2:4]
series = plate_number[4:6]
vehicle_num = plate_number[6:10]

# Check layout logic rules
rule_1 = state_code.isalpha()
rule_2 = district_code.isdigit()
rule_3 = series.isalpha()
rule_4 = vehicle_num.isdigit()
rule_5 = len(plate_number) == 10

if rule_1 and rule_2 and rule_3 and rule_4 and rule_5:
    plate_status = "Valid"
else:
    plate_status = "Invalid"

# Display Output
print(f"Vehicle Number: {plate_number}")
print(f"State Code: {state_code}")
print(f"District Code: {district_code}")
print(f"Series: {series}")
print(f"Vehicle Number: {vehicle_num}")
print()
print(f"Total Letters: {total_letters}")
print(f"Total Digits: {total_digits}")
print()
print(f"Vehicle Number Status: {plate_status}")