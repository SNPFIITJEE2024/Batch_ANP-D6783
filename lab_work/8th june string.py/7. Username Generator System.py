# 7. Username Generator System 
# Problem Statement 
# A student enters: 
# Rahul Sharma 
# Tasks 
# Generate a username using the rules: 
# 1. Remove spaces.  
# 2. Convert to lowercase.  
# 3. Append current year (2026).  
# 4. If username length exceeds 12, keep only first 12 characters.  
# 5. Count vowels in the generated username.  
# 6. Count consonants.  
# 7. Display username statistics.  
# Sample Output 
# Original Name: Rahul Sharma 
 
# Generated Username: 
# rahulsharma2026 
 
# Username Length: 15 
 
# Vowels: 5 
# Consonants: 10 
 
# Status: Username Generated Successfully

# Input Student Name
original_name = "Rahul Sharma"

# Rule 1 & 2: Clear white space spaces and translate to lowercase
clean_name = original_name.replace(" ", "").lower()

# Rule 3: Merge string with the fixed year string block
full_username = clean_name + "2026"

# Rule 4: Enforce max width constraint slice boundary limits
if len(full_username) > 12:
    generated_username = full_username[:12]
else:
    generated_username = full_username

username_length = len(generated_username)

vowel_count = 0
consonant_count = 0

# Count string characters
for char in generated_username:
    if char.isalpha():
        if char in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

# Display Output
print(f"Original Name: {original_name}")
print()
print("Generated Username:")
print(generated_username)
print()
print(f"Username Length: {username_length}")
print()
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print()
print("Status: Username Generated Successfully")