attendance = {}

for i in range(3):
    roll_no = input("Enter roll number: ")
    status = input("Enter Attendance (Present/Absent): ")

    attendance[roll_no] = status

print("\nStudents who are Present:")

for i in attendance:
    if attendance[i] == "Present":
        print(i)