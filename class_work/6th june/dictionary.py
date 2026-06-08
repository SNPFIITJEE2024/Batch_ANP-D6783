#to create a dictionary to store student's data
students = {'std101':"Akash",'std102':"Abhinav",'std103':"Anil",'std104':'Rahul'}

#to display the data
print("Student details : ")
print(students)
print("------------------------------------------")

#to update record of student whose roll number is std103
students['std103'] = 'Rohit'

#to update record of student whose roll number is std105
students['std105'] = 'Rakesh'

print("Student details : ")
print(students)
print("------------------------------------------")

for x in students:
    print(x, ' -> ', students[x])
