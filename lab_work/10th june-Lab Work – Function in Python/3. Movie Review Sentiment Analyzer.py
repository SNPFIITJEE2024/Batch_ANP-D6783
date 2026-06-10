# 3. Movie Review Sentiment Analyzer 
# Problem Statement 
# Movie reviews are stored as follows: 
# reviews = [ 
#     "excellent movie", 
#     "average story", 
#     "excellent acting", 
#     "poor direction", 
#     "excellent visuals", 
#     "poor screenplay", 
#     "good music", 
#     "excellent climax", 
#     "average performance", 
#     "good cinematography" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_sentiments(reviews) 
# Counts: 
# • Excellent  
# • Good  
# • Average  
# • Poor reviews  
# 2. most_common_word(reviews) 
# Returns the most frequently occurring word. 
# 3. longest_review(reviews) 
# Returns the review containing the maximum number of characters. 
# 4. reviews_with_keyword(reviews, keyword) 
# Displays all reviews containing a given keyword. 
# Sample Output 
# Excellent Reviews: 4 
# Good Reviews: 2 
# Average Reviews: 2 
# Poor Reviews: 2 
 
# Most Common Word: 
# excellent 
 
# Longest Review: 
# good cinematography 
 
# Reviews containing 'excellent': 
# excellent movie 
# excellent acting 
# excellent visuals 
# excellent climax


# =====================================================================
# 3. Movie Review Sentiment Analyzer
# =====================================================================

# Our initial array list of text strings containing user movie reviews
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
]


# 1. Function to count occurrences of specific sentiment keywords
def count_sentiments(review_list):
    excellent_count = 0
    good_count = 0
    average_count = 0
    poor_count = 0
    
    for review in review_list:
        # Convert text string to lowercase to make checking reliable
        lower_review = review.lower()
        
        # Look for the target word inside the current string sentence
        if "excellent" in lower_review:
            excellent_count += 1
        elif "good" in lower_review:
            good_count += 1
        elif "average" in lower_review:
            average_count += 1
        elif "poor" in lower_review:
            poor_count += 1
            
    return excellent_count, good_count, average_count, poor_count


# 2. Function to find the single most frequently occurring word
def most_common_word(review_list):
    all_words = []
    
    # Step A: Split each string sentence into individual separate words
    for review in review_list:
        words = review.lower().split()
        for word in words:
            all_words.append(word)
            
    # Step B: Manually find the word with the highest frequency count
    frequent_word = all_words[0]
    max_count = 0
    
    for word in all_words:
        # Count how many times the current word appears in our full word tracker list
        current_word_count = 0
        for match_item in all_words:
            if match_item == word:
                current_word_count += 1
                
        # If this count is higher than our max benchmark, update trackers
        if current_word_count > max_count:
            max_count = current_word_count
            frequent_word = word
            
    return frequent_word


# 3. Function to locate the review string with the absolute maximum character length
def longest_review(review_list):
    longest_string = review_list[0]
    
    for review in review_list:
        # Compare total characters lengths using the standard len() tracking properties
        if len(review) > len(longest_string):
            longest_string = review
            
    return longest_string


# 4. Function to scan, filter, and print reviews holding a specific search keyword
def reviews_with_keyword(review_list, keyword):
    print(f"Reviews containing '{keyword}':")
    
    for review in review_list:
        if keyword.lower() in review.lower():
            print(review)


# =====================================================================
# Execution / Testinggit Program Block
# =====================================================================

# 1. Calculate, extract, and unpack sentiment tracking tallies
exc, gd, avg, pr = count_sentiments(reviews)
print(f"Excellent Reviews: {exc}")
print(f"Good Reviews: {gd}")
print(f"Average Reviews: {avg}")
print(f"Poor Reviews: {pr}")
print()

# 2. Extract and display the word frequency leader token
common = most_common_word(reviews)
print("Most Common Word:")
print(common)
print()

# 3. Print out the longest data log string layout element text
longest = longest_review(reviews)
print("Longest Review:")
print(longest)
print()

# 4. Run substring keyword verification filter lookups matching specific inputs
reviews_with_keyword(reviews, "excellent")