#Problem Statement: Accept marks of 5 subjects. Display: • Total Marks • Percentage • Grade Grade Criteria: Percentage Grade >=90 A+ >=75 A >=60 B >=40 C<40 FailAlso display the number of subjects failed. # Initialize variables to keep track of totals and failures total_marks = 0

failed_subjects_count = 0
number_of_subjects = 5

print(f"--- Enter Marks for {number_of_subjects} Subjects (Out of 100 each) ---")# --- Step 1: Initialize our variables ---
total_marks = 0
failed_subjects = 0
num_of_subjects = 5

print(f"Please enter the marks for all {num_of_subjects} subjects (Out of 100):")
print("-" * 50)

# --- Step 2: Collect marks using a loop ---
for i in range(1, num_of_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    
    # Add current subject marks to the running total
    total_marks += marks
    
    # Check if the student failed this specific subject (passing marks are 40)
    if marks < 40:
        failed_subjects += 1

# --- Step 3: Calculate the overall percentage ---
# Total maximum marks possible is 500 (5 subjects * 100)
percentage = (total_marks / 500) * 100

# --- Step 4: Determine the grade based on criteria ---
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# --- Step 5: Display the final report card output ---
print("\n" + "="*15 + " MARKSHEET SUMMARY " + "="*15)
print(f"Total Marks Scored : {total_marks} / 500")
print(f"Aggregate Percentage: {percentage:.2f}%")
print(f"Final Grade        : {grade}")
print(f"No. of Subjects Failed: {failed_subjects}")
print("=" * 49)

# Loop 5 times to take input for each subject dynamically
for i in range(1, number_of_subjects + 1):
    marks = float(input(f"Enter marks for Subject #{i}: "))
    
    # Add the marks to our running total calculation
    total_marks += marks
    
    # According to grading rules, passing marks are >= 40. 
    # If a subject score is below 40, increment the failure counter.
    if marks < 40:
        failed_subjects_count += 1

# Calculate the overall aggregate percentage
percentage = (total_marks / (number_of_subjects * 100)) * 100

# Determine the final letter grade based on percentage criteria
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display the complete report card layout
print("\n--- Student Performance Report Card ---")
print(f"Total Marks Obtained : {total_marks} / 500")
print(f"Percentage           : {percentage:.2f}%")
print(f"Final Grade Assigned : {grade}")
print(f"Number of Subjects Failed : {failed_subjects_count}")