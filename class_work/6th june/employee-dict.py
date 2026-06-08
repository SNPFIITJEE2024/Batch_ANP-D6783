# '''Problem Statement 
# A company stores employee details in a tuple. Each employee record contains: 
# employees = ( 
#     ("E101", "Anuj", 92), 
#     ("E102", "Rahul", 76), 
#     ("E103", "Priya", 58), 
#     ("E104", "Neha", 88), 
#     ("E105", "Amit", 45) 
# ) 
# Where: 
# • First value = Employee ID  
# • Second value = Employee Name  
# • Third value = Performance Score  
# Tasks 
# Write a Python program to: 
# 1. Display details of employees scoring 80 or above.  
# 2. Count the number of employees who need improvement (score below 60).  
# 3. Find the employee with the highest score.  
# 4. Create a list containing the names of all employees scoring above 75.  
# 5. Display the performance category for each employee:  
# o 90 and above → Excellent  
# o 75 to 89 → Good  
# o 60 to 74 → Average  
# o Below 60 → Needs Improvement  '''


employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

print("Employees Scoring 80 or Above:")
improve = 0

for i in employees:
    if i[2] >= 80:
        print(i[0], i[1], i[2])
    elif i[2]<60:
        improve+=1
        
print("\n")

print("employee needing improvement :" , improve)

print("\n")

print("High performers are : ")
high = []

for i in employees:
    if i[2] >= 75:
        high.append(i[1])
        
print(high,'\n')

print("performance category:")

for i in employees:
    if i[2]>=90:
        print(i[1],"--->","excellent")
    elif i[2]>=75:
        print(i[1],"--->","good")
    elif i[2]>=60:
        print(i[1],"--->","average")
    else:
        print(i[1],"--->","need improvement")
print("\n")

top = employees[0]
for e in employees:
    if e[2] > top[2]:
        top = e

print("Highest Performer:")
print(top[0], top[1], top[2])
print()