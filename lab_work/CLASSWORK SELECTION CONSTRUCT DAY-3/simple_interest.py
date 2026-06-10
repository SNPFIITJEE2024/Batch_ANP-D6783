# Simple Interest Calculator (no negative values allowed)

P = float(input("Enter Principal: "))

while P < 0:
    print("Negative not allowed!")
    P = float(input("Enter Principal again: "))

R = float(input("Enter Rate: "))

while R < 0:
    print("Negative not allowed!")
    R = float(input("Enter Rate again: "))

T = float(input("Enter Time: "))

while T < 0:
    print("Negative not allowed!")
    T = float(input("Enter Time again: "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)