# Rectangle Area and Perimeter 

L = float(input("Enter Length: "))

while L < 0:
    print("Negative not allowed!")
    L = float(input("Enter Length again: "))

W = float(input("Enter Width: "))

while W < 0:
    print("Negative not allowed!")
    W = float(input("Enter Width again: "))

area = L * W
perimeter = 2 * (L + W)

print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)