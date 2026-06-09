# 10. Text Compression Analyzer 
# Problem Statement 
# A compressed message is given: 
# AAABBBCCCDDDAAA 
# Tasks 
# Write a program to: 
# 1. Count occurrences of each character.  
# 2. Create a dictionary of character frequencies.  
# 3. Display unique characters.  
# 4. Find the most frequent character.  
# 5. Create a compressed output:  
# A3B3C3D3A3 
# 6. Calculate compression ratio.  
# Sample Output 
# Original Text: 
# AAABBBCCCDDDAAA 
 
# Character Frequencies: 
# A -> 6 
# B -> 3 
# C -> 3 
# D -> 3 
 
# Unique Characters: 
# ['A', 'B', 'C', 'D'] 
 
# Most Frequent Character: A 
 
# Compressed Output: 
# A3B3C3D3A3 
 
# Original Length: 15 
# Compressed Length: 10 
 
# Compression Ratio: 66.67%

# Input Compressed Message
original_text = "AAABBBCCCDDDAAA"

original_length = len(original_text)
unique_chars = []

# Build unique items array manually without sets or dicts
for char in original_text:
    if char not in unique_chars:
        unique_chars.append(char)

# Find the most frequent character using standard .count() operations
most_frequent_char = unique_chars[0]
highest_count = 0

for char in unique_chars:
    current_count = original_text.count(char)
    if current_count > highest_count:
        highest_count = current_count
        most_frequent_char = char

# Build sequential compression string manually using a look-ahead loop tracker
compressed_output = ""

if original_text:
    current_run_char = original_text[0]
    run_length = 1
    
    for i in range(1, len(original_text)):
        if original_text[i] == current_run_char:
            run_length += 1
        else:
            compressed_output += current_run_char + str(run_length)
            current_run_char = original_text[i]
            run_length = 1
            
    # Append final remaining trailing sequence block elements
    compressed_output += current_run_char + str(run_length)

compressed_length = len(compressed_output)
compression_ratio = (compressed_length / original_length) * 100

# Display Output
print("Original Text:")
print(original_text)
print()
print("Character Frequencies:")
for char in unique_chars:
    print(f"{char} -> {original_text.count(char)}")
print()
print("Unique Characters:")
print(unique_chars)
print()
print(f"Most Frequent Character: {most_frequent_char}")
print()
print("Compressed Output:")
print(compressed_output)
print()
print(f"Original Length: {original_length}")
print(f"Compressed Length: {compressed_length}")
print()
print(f"Compression Ratio: {compression_ratio:.2f}%")