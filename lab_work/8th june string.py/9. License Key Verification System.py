# 9. License Key Verification System 
# Problem Statement 
# A software license key is entered: 
# ABCD-EFGH-IJKL-MNOP 
# Tasks 
# Write a program to: 
# 1. Verify there are exactly 4 groups.  
# 2. Verify each group contains exactly 4 characters.  
# 3. Count total letters.  
# 4. Count vowels.  
# 5. Remove hyphens and display the merged key.  
# 6. Create a list containing all groups.  
# 7. Display whether the key format is valid.  
# Sample Output 
# License Key: 
# ABCD-EFGH-IJKL-MNOP 
 
# Groups: 
# ['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
 
# Number of Groups: 4 
 
# Total Letters: 16 
# Total Vowels: 4 
 
# Merged Key: 
# ABCDEFGHIJKLMNOP 
 
# License Key Status: Valid

# Input Software License Key
license_key = "ABCD-EFGH-IJKL-MNOP"

# Create a clean string without hyphens
merged_key = license_key.replace("-", "")

# Break into groups using split
groups_list = license_key.split("-")
number_of_groups = len(groups_list)

total_letters = 0
total_vowels = 0
all_groups_valid_len = True

# Read elements step-by-step
for group in groups_list:
    if len(group) != 4:
        all_groups_valid_len = False
        
    for char in group:
        if char.isalpha():
            total_letters += 1
            if char.lower() in "aeiou":
                total_vowels += 1

# Final Format Verification Checks
if number_of_groups == 4 and all_groups_valid_len:
    key_status = "Valid"
else:
    key_status = "Invalid"

# Display Output
print("License Key:")
print(license_key)
print()
print("Groups:")
print(groups_list)
print()
print(f"Number of Groups: {number_of_groups}")
print()
print(f"Total Letters: {total_letters}")
print(f"Total Vowels: {total_vowels}")
print()
print("Merged Key:")
print(merged_key)
print()
print(f"License Key Status: {key_status}")