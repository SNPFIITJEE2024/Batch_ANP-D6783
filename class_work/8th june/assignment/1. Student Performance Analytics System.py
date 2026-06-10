# 1. Student Performance Analytics System 
# Problem Statement 
# A coaching institute wants to analyze student performance. 
# Store details of at least 30 students in a dictionary. 
# Example Structure 
# students = { 
#     "S101": {"name": "Anuj", "marks": 85}, 
#     "S102": {"name": "Rahul", "marks": 72} 
# } 
# Requirements 
# 1. Display all student records.  
# 2. Search a student using Student ID.  
# 3. Add a new student.  
# 4. Update marks of an existing student.  
# 5. Delete a student.  
# 6. Find topper and lowest scorer.  
# 7. Calculate class average.  
# 8. Count pass and fail students.  
# 9. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)  
# 10. Display students scoring above average.  
# 11. Display top 5 performers.  
# 12. Create a separate dictionary for scholarship students (marks > 85).  
# Expected Learning 
# • Nested Dictionaries  
# • Dictionary Traversal  
# • Searching  
# • Aggregation  
# • Report Generation 



# # =====================================================================
# # Student Performance Analytics System
# # =====================================================================

# # Step 1: Initialize the nested dictionary with 30 student records
# students = {
#     "S101": {"name": "Anuj", "marks": 85},
#     "S102": {"name": "Rahul", "marks": 72},
#     "S103": {"name": "Priya", "marks": 94},
#     "S104": {"name": "Sneha", "marks": 48},
#     "S105": {"name": "Amit", "marks": 78},
#     "S106": {"name": "Rohit", "marks": 63},
#     "S107": {"name": "Deepak", "marks": 91},
#     "S108": {"name": "Neha", "marks": 55},
#     "S109": {"name": "Vikas", "marks": 82},
#     "S110": {"name": "Jyoti", "marks": 74},
#     "S111": {"name": "Manish", "marks": 41},
#     "S112": {"name": "Kiran", "marks": 89},
#     "S113": {"name": "Ravi", "marks": 67},
#     "S114": {"name": "Pooja", "marks": 96},
#     "S115": {"name": "Sanjay", "marks": 73},
#     "S116": {"name": "Aarti", "marks": 88},
#     "S117": {"name": "Rajesh", "marks": 52},
#     "S118": {"name": "Sunita", "marks": 79},
#     "S119": {"name": "Vijay", "marks": 35},
#     "S120": {"name": "Anjali", "marks": 90},
#     "S121": {"name": "Ajay", "marks": 76},
#     "S122": {"name": "Divya", "marks": 84},
#     "S123": {"name": "Arjun", "marks": 61},
#     "S124": {"name": "Kavita", "marks": 45},
#     "S125": {"name": "Preeti", "marks": 80},
#     "S126": {"name": "Manoj", "marks": 69},
#     "S127": {"name": "Swati", "marks": 92},
#     "S128": {"name": "Alok", "marks": 58},
#     "S129": {"name": "Ritu", "marks": 87},
#     "S130": {"name": "Nitin", "marks": 70}
# }

# # 1. Display all student records
# def display_all_students():
#     print("\n--- All Student Records ---")
#     print(f"{'ID':<10}{'Name':<15}{'Marks':<10}")
#     print("-" * 35)
#     for sid, info in students.items():
#         print(f"{sid:<10}{info['name']:<15}{info['marks']:<10}")

# # 2. Search a student using Student ID
# def search_student(sid):
#     print(f"\n--- Searching for ID: {sid} ---")
#     if sid in students:
#         print(f"Found! Name: {students[sid]['name']}, Marks: {students[sid]['marks']}")
#     else:
#         print("Error: Student ID not found.")

# # 3. Add a new student
# def add_student(sid, name, marks):
#     print(f"\n--- Adding New Student: {sid} ---")
#     if sid in students:
#         print("Error: A student with this ID already exists.")
#     else:
#         students[sid] = {"name": name, "marks": marks}
#         print(f"Successfully added {name}!")

# # 4. Update marks of an existing student
# def update_marks(sid, new_marks):
#     print(f"\n--- Updating Marks for ID: {sid} ---")
#     if sid in students:
#         old_marks = students[sid]['marks']
#         students[sid]['marks'] = new_marks
#         print(f"Updated {students[sid]['name']}'s marks from {old_marks} to {new_marks}.")
#     else:
#         print("Error: Student ID not found.")

# # 5. Delete a student
# def delete_student(sid):
#     print(f"\n--- Deleting Student ID: {sid} ---")
#     if sid in students:
#         removed = students.pop(sid)
#         print(f"Successfully removed {removed['name']} from the records.")
#     else:
#         print("Error: Student ID not found.")

# # 6. Find topper and lowest scorer
# def find_topper_and_lowest():
#     print("\n--- Topper & Lowest Scorer ---")
#     # Using python's max/min functions tracking by the nested 'marks' key
#     topper_id = max(students, key=lambda k: students[k]['marks'])
#     lowest_id = min(students, key=lambda k: students[k]['marks'])
    
#     print(f"Topper: {students[topper_id]['name']} ({topper_id}) with {students[topper_id]['marks']} marks.")
#     print(f"Lowest Scorer: {students[lowest_id]['name']} ({lowest_id}) with {students[lowest_id]['marks']} marks.")

# # 7. Helper function to calculate class average
# def calculate_average():
#     total_marks = sum(info['marks'] for info in students.values())
#     return total_marks / len(students)

# # 8. Count pass and fail students (Passing mark is 50)
# def count_pass_fail():
#     print("\n--- Pass / Fail Stats ---")
#     pass_count = 0
#     fail_count = 0
#     for info in students.values():
#         if info['marks'] >= 50:
#             pass_count += 1
#         else:
#             fail_count += 1
#     print(f"Passed Students: {pass_count}")
#     print(f"Failed Students: {fail_count}")

# # 9. Generate and display grades
# def generate_grades():
#     print("\n--- Student Grades ---")
#     print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
#     print("-" * 30)
#     for info in students.values():
#         marks = info['marks']
#         if marks >= 90:
#             grade = 'A'
#         elif marks >= 75:
#             grade = 'B'
#         elif marks >= 50:
#             grade = 'C'
#         else:
#             grade = 'F'
#         print(f"{info['name']:<15}{marks:<10}{grade:<5}")

# # 10. Display students scoring above average
# def display_above_average():
#     avg = calculate_average()
#     print(f"\n--- Students Scoring Above Class Average ({avg:.2f}) ---")
#     for sid, info in students.items():
#         if info['marks'] > avg:
#             print(f"{info['name']} ({sid}): {info['marks']}")

# # 11. Display top 5 performers
# def display_top_5():
#     print("\n--- Top 5 Performers ---")
#     # Sort students descending by their marks and grab the first 5 records
#     sorted_students = sorted(students.items(), key=lambda item: item[1]['marks'], reverse=True)
#     for i in range(5):
#         sid, info = sorted_students[i]
#         print(f"{i+1}. {info['name']} ({sid}) - Marks: {info['marks']}")

# # 12. Create a separate dictionary for scholarship students (marks > 85)
# def get_scholarship_students():
#     print("\n--- Creating Scholarship Dictionary (Marks > 85) ---")
#     scholarship_dict = {sid: info for sid, info in students.items() if info['marks'] > 85}
    
#     # Let's print out the new dictionary to verify it works
#     for sid, info in scholarship_dict.items():
#         print(f"Scholarship Holder -> {sid}: {info}")
#     return scholarship_dict


# # =====================================================================
# # Execution / Testing Dashboard
# # =====================================================================

# # 1. Show initial pool of records
# display_all_students()

# # 2. Search functionality demo
# search_student("S103")
# search_student("S999") # Testing non-existent ID

# # 3. Add a new record
# add_student("S131", "Tanuj", 98)

# # 4. Update an existing record
# update_marks("S101", 87)

# # 5. Delete a record
# delete_student("S119") 

# # 6 & 7. Aggregations (Topper, Lowest, Average)
# find_topper_and_lowest()
# print(f"\nClass Average Marks: {calculate_average():.2f}")

# # 8. Pass/Fail Counter
# count_pass_fail()

# # 9. Print out full Grade sheets
# generate_grades()

# # 10. Show above average performers
# display_above_average()

# # 11. Print the top leaderboard elite
# display_top_5()

# # 12. Spin up the specific scholarship object structure
# scholarships = get_scholarship_students()



# =====================================================================
# 1. Student Performance Analytics System (Menu-Driven)
# =====================================================================

# Initialize the dictionary with 30 student records
students = {
    "S101": {"name": "Anuj", "marks": 85}, "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 94}, "S104": {"name": "Sneha", "marks": 48},
    "S105": {"name": "Amit", "marks": 78}, "S106": {"name": "Rohit", "marks": 63},
    "S107": {"name": "Deepak", "marks": 91}, "S108": {"name": "Neha", "marks": 55},
    "S109": {"name": "Vikas", "marks": 82}, "S110": {"name": "Jyoti", "marks": 74},
    "S111": {"name": "Manish", "marks": 41}, "S112": {"name": "Kiran", "marks": 89},
    "S113": {"name": "Ravi", "marks": 67}, "S114": {"name": "Pooja", "marks": 96},
    "S115": {"name": "Sanjay", "marks": 73}, "S116": {"name": "Aarti", "marks": 88},
    "S117": {"name": "Rajesh", "marks": 52}, "S118": {"name": "Sunita", "marks": 79},
    "S119": {"name": "Vijay", "marks": 35}, "S120": {"name": "Anjali", "marks": 90},
    "S121": {"name": "Ajay", "marks": 76}, "S122": {"name": "Divya", "marks": 84},
    "S123": {"name": "Arjun", "marks": 61}, "S124": {"name": "Kavita", "marks": 45},
    "S125": {"name": "Preeti", "marks": 80}, "S126": {"name": "Manoj", "marks": 69},
    "S127": {"name": "Swati", "marks": 92}, "S128": {"name": "Alok", "marks": 58},
    "S129": {"name": "Ritu", "marks": 87}, "S130": {"name": "Nitin", "marks": 70}
}

while True:
    print("\n=========================================")
    print("   STUDENT PERFORMANCE ANALYTICS MENU    ")
    print("=========================================")
    print("1. Display All Student Records")
    print("2. Search Student by ID")
    print("3. Add New Student")
    print("4. Update Student Marks")
    print("5. Delete Student Record")
    print("6. Find Topper and Lowest Scorer")
    print("7. Calculate Class Average")
    print("8. Count Pass and Fail Students")
    print("9. Generate Grade Report")
    print("10. Display Students Scoring Above Average")
    print("11. Display Top 5 Performers")
    print("12. Generate Scholarship Dictionary (>85)")
    print("13. Exit Program")
    print("=========================================")
    
    choice = input("Enter your choice (1-13): ")
    
    if choice == "1":
        print(f"\n{ 'ID':<10 }{ 'Name':<15 }{ 'Marks':<10 }")
        print("-" * 35)
        for sid, info in students.items():
            print(f"{ sid:<10 }{ info['name']:<15 }{ info['marks']:<10 }")
            
    elif choice == "2":
        sid = input("Enter Student ID to search: ")
        if sid in students:
            print(f"\n[Found] Name: {students[sid]['name']}, Marks: {students[sid]['marks']}")
        else:
            print("\n[Error] Student ID not found.")
            
    elif choice == "3":
        sid = input("Enter New Student ID: ")
        if sid in students:
            print("\n[Error] ID already exists!")
        else:
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))
            students[sid] = {"name": name, "marks": marks}
            print(f"\n[Success] Added {name} successfully.")
            
    elif choice == "4":
        sid = input("Enter Student ID to update: ")
        if sid in students:
            new_marks = int(input("Enter New Marks: "))
            students[sid]['marks'] = new_marks
            print("\n[Success] Marks updated successfully.")
        else:
            print("\n[Error] Student ID not found.")
            
    elif choice == "5":
        sid = input("Enter Student ID to delete: ")
        if sid in students:
            removed = students.pop(sid)
            print(f"\n[Deleted] Removed {removed['name']} from system database.")
        else:
            print("\n[Error] Student ID not found.")
            
    elif choice == "6":
        # Manual Max/Min extraction loops without built-ins
        topper_id = None
        lowest_id = None
        
        for sid, info in students.items():
            if topper_id is None or info['marks'] > students[topper_id]['marks']:
                topper_id = sid
            if lowest_id is None or info['marks'] < students[lowest_id]['marks']:
                lowest_id = sid
                
        print(f"\n🏆 Topper: {students[topper_id]['name']} ({topper_id}) - {students[topper_id]['marks']} Marks")
        print(f"📉 Lowest: {students[lowest_id]['name']} ({lowest_id}) - {students[lowest_id]['marks']} Marks")
        
    elif choice == "7":
        total_marks = 0
        count = 0
        for info in students.values():
            total_marks += info['marks']
            count += 1
        avg = total_marks / count if count > 0 else 0
        print(f"\n📈 Class Average Marks: {avg:.2f}")
        
    elif choice == "8":
        passed = 0
        failed = 0
        for info in students.values():
            if info['marks'] >= 50:
                passed += 1
            else:
                failed += 1
        print(f"\n✅ Passed: {passed} | ❌ Failed: {failed}")
        
    elif choice == "9":
        print(f"\n{ 'Name':<15 }{ 'Marks':<10 }{ 'Grade':<5 }")
        print("-" * 30)
        for info in students.values():
            m = info['marks']
            if m >= 90: grade = "A"
            elif m >= 75: grade = "B"
            elif m >= 50: grade = "C"
            else: grade = "F"
            print(f"{ info['name']:<15 }{ m:<10 }{ grade:<5 }")
            
    elif choice == "10":
        total_marks = 0
        count = 0
        for info in students.values():
            total_marks += info['marks']
            count += 1
        avg = total_marks / count
        
        print(f"\n--- Scoring Above Average ({avg:.2f}) ---")
        for sid, info in students.items():
            if info['marks'] > avg:
                print(f" - {info['name']} ({sid}): {info['marks']}")
                
    elif choice == "11":
        # Converting dictionary data into an indexable tracking array list
        student_list = []
        for sid, info in students.items():
            student_list.append([sid, info['name'], info['marks']])
            
        # Implementing a manual Bubble Sort descending algorithm
        n = len(student_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if student_list[j][2] < student_list[j + 1][2]:
                    # Swap items
                    student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
                    
        print("\n🏆 --- Top 5 Performers Leaderboard ---")
        for i in range(5 if len(student_list) >= 5 else len(student_list)):
            print(f" #{i+1} {student_list[i][1]} ({student_list[i][0]}) - Marks: {student_list[i][2]}")
            
    elif choice == "12":
        scholarships = {}
        for sid, info in students.items():
            if info['marks'] > 85:
                scholarships[sid] = {"name": info['name'], "marks": info['marks']}
        print("\n[System] New Scholarship Dictionary Generated:")
        print(scholarships)
        
    elif choice == "13":
        print("\nExiting Student Workspace Dashboard. Goodbye!")
        break
    else:
        print("\n[Invalid] Selection outside menu bounds. Try again.")