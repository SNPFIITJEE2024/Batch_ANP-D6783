# ==========================================
# 4. Tournament Runs Analytics Dashboard
# ==========================================

# Initializing data for runs scored by players in the tournament
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 

# ------------------------------------------
# Task 1: Display players scoring more than 500 runs.
# ------------------------------------------
print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    if score > 500:
        print(player)
print() # Layout spacing


# ------------------------------------------
# Task 2 & 3: Find the Orange Cap winner (highest) and lowest scorer.
# ------------------------------------------
# Initializing baseline boundaries using the first player in our dataset
first_player = list(runs.keys())[0]
first_score = runs[first_player]

orange_cap_winner = first_player
max_runs = first_score

lowest_scorer = first_player
min_runs = first_score

# Traversing the dataset to find the highest and lowest scores
for player, score in runs.items():
    # Updating highest scorer track
    if score > max_runs:
        max_runs = score
        orange_cap_winner = player
        
    # Updating lowest scorer track
    if score < min_runs:
        min_runs = score
        lowest_scorer = player

print(f"Orange Cap Winner: {orange_cap_winner} ({max_runs})\n")
print(f"Lowest Scorer: {lowest_scorer} ({min_runs})\n")


# ------------------------------------------
# Task 4: Calculate total runs scored in the tournament.
# ------------------------------------------
total_tournament_runs = 0
for score in runs.values():
    total_tournament_runs += score

print(f"Total Tournament Runs: {total_tournament_runs}\n")


# ------------------------------------------
# Task 5: Create a list of players scoring below 400.
# ------------------------------------------
below_400_list = []
for player, score in runs.items():
    if score < 400:
        below_400_list.append(player)

print("Players Scoring Below 400:")
print(below_400_list)
print()


# ------------------------------------------
# Task 6: Count players scoring between 400 and 600 runs (inclusive).
# ------------------------------------------
mid_range_count = 0
for score in runs.values():
    if 400 <= score <= 600:
        mid_range_count += 1

print(f"Players Between 400 and 600 Runs: {mid_range_count}")