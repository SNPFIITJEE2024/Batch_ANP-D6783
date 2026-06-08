# '''Problem Statement 
# A flight reservation system stores passenger records as tuples: 
# bookings = ( 
#     ("P101", "Delhi", "Confirmed"), 
#     ("P102", "Mumbai", "Waiting"), 
#     ("P103", "Delhi", "Confirmed"), 
#     ("P104", "Chennai", "Cancelled"), 
#     ("P105", "Mumbai", "Confirmed"), 
#     ("P106", "Delhi", "Waiting") 
# ) 
# Where: 
# • Passenger ID  
# • Destination  
# • Booking Status  
# Tasks 
# Write a Python program to: 
# 1. Display all passengers whose booking status is Confirmed.  
# 2. Count the number of passengers travelling to Delhi.  
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.  
# 4. Create a list containing passenger IDs with Waiting status.  
# 5. Determine which destination has the highest number of bookings.  '''

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Confirmed passengers
print("Confirmed Passengers:")
for i in bookings:
    if i[2] == "Confirmed":
        print(i[0], i[1])

print()

# 2. Count passengers travelling to Delhi
count_delhi = 0
for i in bookings:
    if i[1] == "Delhi":
        count_delhi += 1

print("Passengers Travelling to Delhi:", count_delhi)
print()

# 3. Count booking statuses
confirmed = waiting = cancelled = 0

for i in bookings:
    if i[2] == "Confirmed":
        confirmed += 1
    elif i[2] == "Waiting":
        waiting += 1
    elif i[2] == "Cancelled":
        cancelled += 1

print("Confirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)
print()

# 4. Waiting list passenger IDs
waiting_list = []
for i in bookings:
    if i[2] == "Waiting":
        waiting_list.append(i[0])

print("Waiting List:")
print(waiting_list)
print()

# 5. Most booked destination

delhi = 0
mumbai = 0
chennai = 0

for i in bookings:
    if i[1] == "Delhi":
        delhi += 1
    elif i[1] == "Mumbai":
        mumbai += 1
    elif i[1] == "Chennai":
        chennai += 1

if delhi > mumbai and delhi > chennai:
    print("Most Booked Destination:\nDelhi")

elif mumbai > delhi and mumbai > chennai:
    print("Most Booked Destination:\nMumbai")

else:
    print("Most Booked Destination:\nChennai")