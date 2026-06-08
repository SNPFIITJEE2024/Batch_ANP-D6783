attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0
# counting present and absent
for i in attendance:
    if i == 'P':
        present += 1
    else:
        absent += 1

percentage = (present / len(attendance)) * 100

print("Present days =", present)
print("Absent days =", absent)
print("Attendance Percentage =", percentage, "%")
# eligibilty checking
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

print("Absent positions are:")
for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i)