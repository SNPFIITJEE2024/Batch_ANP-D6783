# '''Problem Statement 
# Employee data is stored as tuples: 
# employees = [ 
#     ("Rahul", 35000), 
#     ("Priya", 55000), 
#     ("Amit", 42000), 
#     ("Neha", 65000) 
# ] 
# Write a program to: 
# • Display employees earning above ₹50,000.  
# • Find the highest-paid employee.  
# • Calculate total salary expenditure.  
# • Count employees earning below ₹40,000. '''

employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
]
total = 0
count = 0
highest = employees[0]
print("Employees having salary greater then 50000 :")
for i in employees:
    total += i[1]
    if i[1]>highest[1]:
        highest=i
    if i[1] > 50000:
        print(f" {i[0]} ")
    elif i[1]<40000:
        count+=1
print(f"\ntotal salary is : {total}")
print(f"\nemployees earning under then 40k : {count}")
print(f"\nhighest paid employee is : {highest[0]}")