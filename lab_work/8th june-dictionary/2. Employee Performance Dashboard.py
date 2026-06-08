# ==========================================
# 2. Employee Performance Dashboard 
# ==========================================

# Initializing the employee performance tracking dictionary
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 

# ------------------------------------------
# Task 1: Display employees scoring above 80.
# ------------------------------------------
print("Employees Scoring Above 80:")
for emp_id, score in performance.items():
    if score > 80:
        print(emp_id)
print() # Layout spacing


# ------------------------------------------
# Task 3: Find the top performer.
# ------------------------------------------
# Setting initial boundary trackers from the first element
first_emp = list(performance.keys())[0]
best_emp = first_emp
max_score = performance[first_emp]

for emp_id, score in performance.items():
    if score > max_score:
        max_score = score
        best_emp = emp_id

print(f"Top Performer: {best_emp} ({max_score})\n")


# ------------------------------------------
# Task 2: Count employees needing improvement (score < 60).
# ------------------------------------------
needs_improvement_count = 0
for score in performance.values():
    if score < 60:
        needs_improvement_count += 1

print(f"Employees Needing Improvement: {needs_improvement_count}\n")


# ------------------------------------------
# Task 4: Calculate average performance score.
# ------------------------------------------
total_score = 0
total_employees = len(performance)

for score in performance.values():
    total_score += score

# Calculating final mean value
average_score = total_score / total_employees
print(f"Average Score: {average_score:.1f}\n")


# ------------------------------------------
# Task 5: Create and populate separate rating breakdown lists.
# ------------------------------------------
excellent_list = []
good_list = []
average_list = []
poor_list = []

for emp_id, score in performance.items():
    if score >= 90:
        excellent_list.append(emp_id)
    elif 75 <= score <= 89:
        good_list.append(emp_id)
    elif 60 <= score <= 74:
        average_list.append(emp_id)
    else: # This covers scores strictly < 60
        poor_list.append(emp_id)

print("Excellent:")
print(excellent_list)
print("\nGood:")
print(good_list)
print("\nAverage:")
print(average_list)
print("\nPoor:")
print(poor_list)