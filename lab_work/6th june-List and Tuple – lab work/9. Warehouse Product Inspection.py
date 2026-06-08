products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for i in products:
    if i[1] == "Pass":
        passed += 1
    else:
        failed += 1
        print(i[0])

        if failed == 3:
            print("3 failures found. Stopping check.")
            break

print("Passed Products =", passed)
print("Failed Products =", failed)

percentage = (passed / len(products)) * 100
print("Pass Percentage =", percentage, "%")