passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed = 0
waiting = 0

confirmed_list = []
waiting_list = []

print("Waiting-list Passengers:")
for i in passengers:
    if i[1] == "Waiting":
        print(i[0])

for i in passengers:
    if i[1] == "Confirmed":
        confirmed += 1
        confirmed_list.append(i[0])
    else:
        waiting += 1
        waiting_list.append(i[0])

print("Confirmed Passengers =", confirmed)
print("Waiting Passengers =", waiting)

name = input("Enter passenger name: ")

for i in passengers:
    if i[0] == name and i[1] == "Confirmed":
        print(name, "has a confirmed ticket")
        break
else:
    print(name, "does not have a confirmed ticket")

print("Confirmed List =", confirmed_list)
print("Waiting List =", waiting_list)