# 8. String-Based Attendance Tracker 
# Problem Statement 
# Attendance of a student for 15 days is represented as: 
# PPAPPPAAPPPPAPP 
# Where: 
# • P = Present  
# • A = Absent  
# Tasks 
# Write a program to: 
# 1. Count Present and Absent days.  
# 2. Calculate attendance percentage.  
# 3. Find the longest consecutive streak of Presence.  
# 4. Find the longest consecutive streak of Absence.  
# 5. Determine whether attendance is below 75%.  
# Sample Output 
# Attendance Record: 
# PPAPPPAAPPPPAPP 
 
# Present Days: 11 
# Absent Days: 4 
 
# Attendance Percentage: 73.33% 
 
# Longest Present Streak: 4 
# Longest Absent Streak: 2 
 
# Attendance Status: Below 75%

# Input Attendance Record (15 days)
attendance_record = "PPAPPPAAPPPPAPP"

present_days = 0
absent_days = 0

# Basic counting loop
for day in attendance_record:
    if day == 'P':
        present_days += 1
    elif day == 'A':
        absent_days += 1

# Calculate basic evaluation score percentage
total_days = len(attendance_record)
attendance_percentage = (present_days / total_days) * 100

# Track consecutive patterns manually using temporary tracking variables
max_p_streak = 0
current_p_streak = 0

max_a_streak = 0
current_a_streak = 0

for day in attendance_record:
    if day == 'P':
        current_p_streak += 1
        current_a_streak = 0 # Reset absent sequence tracker
        if current_p_streak > max_p_streak:
            max_p_streak = current_p_streak
    elif day == 'A':
        current_a_streak += 1
        current_p_streak = 0 # Reset present sequence tracker
        if current_a_streak > max_a_streak:
            max_a_streak = current_a_streak

if attendance_percentage < 75.0:
    attendance_status = "Below 75%"
else:
    attendance_status = "Good"

# Display Output
print("Attendance Record:")
print(attendance_record)
print()
print(f"Present Days: {present_days}")
print(f"Absent Days: {absent_days}")
print()
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
print()
print(f"Longest Present Streak: {max_p_streak}")
print(f"Longest Absent Streak: {max_a_streak}")
print()
print(f"Attendance Status: {attendance_status}")