# 3. Chat Message Analytics 
# Problem Statement 
# A chat application stores a message: 
# Python is awesome and Python is easy to learn 
# Tasks 
# Write a program to: 
# 1. Count total characters.  
# 2. Count total words.  
# 3. Find the longest word.  
# 4. Find the shortest word.  
# 5. Count how many times the word "Python" appears.  
# 6. Create a list of words having more than 4 characters.  
# 7. Display all words starting with a vowel.  
# 8. Count the number of vowels and consonants.  
# Sample Output 
# Message: 
# Python is awesome and Python is easy to learn 
 
# Total Characters: 45 
# Total Words: 8 
 
# Longest Word: awesome 
# Shortest Word: is 
 
# Occurrences of Python: 2 
 
# Words Longer Than 4 Characters: 
# ['Python', 'awesome', 'Python', 'learn'] 
 
# Vowels: 16 
# Consonants: 22

# Input chat message
message = "Python is awesome and Python is easy to learn"

# Get base calculations
total_chars = len(message)
words_list = message.split()
total_words = len(words_list)

# Setup initial baselines for comparisons
longest_word = words_list[0]
shortest_word = words_list[0]
python_count = 0

long_words_list = []
vowel_count = 0
consonant_count = 0

# Scan the word list
for word in words_list:
    if word == "Python":
        python_count += 1
        
    if len(word) > 4:
        long_words_list.append(word)
        
    if len(word) > len(longest_word):
        longest_word = word
        
    if len(word) < len(shortest_word):
        shortest_word = word

# Scan the raw text message line for character counts
for char in message.lower():
    if char.isalpha(): # Only look at alphabetical letters
        if char in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

# Display Output
print("Message:")
print(message)
print()
print(f"Total Characters: {total_chars}")
print(f"Total Words: {total_words}")
print()
print(f"Longest Word: {longest_word}")
print(f"Shortest Word: {shortest_word}")
print()
print(f"Occurrences of Python: {python_count}")
print()
print("Words Longer Than 4 Characters:")
print(long_words_list)
print()
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")