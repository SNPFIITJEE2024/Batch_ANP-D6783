# '''Problem Statement 
# Parking slots are represented as: 
# slots = [1, 0, 1, 1, 0, 0, 1, 0] 
# Where: 
# • 1 = Occupied  
# • 0 = Available  
# Write a program to: 
# • Count occupied and available slots.  
# • Find the first available slot.  
# • Display all available slot numbers.  
# • Check whether parking occupancy exceeds 75%.'''

slots = [1, 0, 1, 1, 0, 0, 1, 0] 
occupied = 0
available = 0
availSeat = []
# counting seats
for i in range(len(slots)):
    if slots[i] == 1:
        occupied += 1
    else:
        available += 1
        availSeat.append(i+1)
print(f"occupied seats are {occupied}")
print(f"available seats are : {available}")

# for first available seat 
firstSeat = slots.index(0) + 1
print("first available slot is at : ",firstSeat)

# to display all available seat numbers 
print(f"all available seat are : {availSeat}")

if available % len(slots) > 7.5:
    print("yes packing exceed 75 %")
else:
    print("there is a lot space ")