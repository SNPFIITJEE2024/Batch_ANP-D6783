# 5. Product Review Analyzer 
# Problem Statement 
# A customer submits a review: 
# This product is excellent excellent excellent and very useful 
# Tasks 
# Write a program to: 
# 1. Count total words.  
# 2. Create a dictionary containing word frequencies.  
# 3. Find the most frequently used word.  
# 4. Find all words appearing only once.  
# 5. Count words having more than 5 characters.  
# 6. Display words in reverse order.  
# 7. Create a list of unique words.  
 
# Sample Output 
# Total Words: 8 
 
# Word Frequencies: 
# This -> 1 
# product -> 1 
# is -> 1 
# excellent -> 3 
# and -> 1 
# very -> 1 
# useful -> 1 
 
# Most Frequent Word: excellent 
 
# Words Appearing Once: 
# ['This', 'product', 'is', 'and', 'very', 'useful'] 
 
# Unique Words: 
# ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']

# Input Customer Review
review = "This product is excellent excellent excellent and very useful"

words_list = review.split()
total_words = len(words_list)

unique_words = []
single_occurrence_words = []
long_words_count = 0

# Build unique word list and count long words
for word in words_list:
    if word not in unique_words:
        unique_words.append(word)
        
    if len(word) > 5:
        long_words_count += 1

# Identify words appearing only once manually using .count()
for word in unique_words:
    if words_list.count(word) == 1:
        single_occurrence_words.append(word)

# Find the most frequent word manually
most_frequent_word = words_list[0]
highest_count = 0

for word in unique_words:
    current_count = words_list.count(word)
    if current_count > highest_count:
        highest_count = current_count
        most_frequent_word = word

# Reverse word order using string list slicing sequence
reversed_words = words_list[::-1]

# Display Output
print(f"Total Words: {total_words}")
print()
print("Word Frequencies:")
for word in unique_words:
    print(f"{word} -> {words_list.count(word)}")
print()
print(f"Most Frequent Word: {most_frequent_word}")
print()
print("Words Appearing Once:")
print(single_occurrence_words)
print()
print("Unique Words:")
print(unique_words)