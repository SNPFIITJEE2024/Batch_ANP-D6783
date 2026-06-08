passengers = [12, 18, 25, 30, 28, 15, 8]

# Busiest stop
maximum = max(passengers)
print("Busiest stop:", passengers.index(maximum) + 1)

# Stops with fewer than 10 passengers
print("Stops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Average passengers
average = sum(passengers) / len(passengers)
print("Average passengers =", average)

# Check if any stop exceeded 25 passengers
flag = False
for i in passengers:
    if i > 25:
        flag = True
        break

if flag:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")