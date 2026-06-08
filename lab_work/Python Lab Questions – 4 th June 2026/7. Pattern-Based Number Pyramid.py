#7. Pattern-Based Number Pyramid Problem Statement: Accept the number of rows and print the following pattern: For Input:5 Output: 1 12 123 1234 12345 Challenge: Print the reverse pattern as well
# --- Step 1: Initialize our variables ---
# --- Step 1: Take input from the user ---
rows = int(input("Enter the number of rows for the pyramid: "))

# --- Step 2: Print the Forward Pattern ---
print("\n--- Forward Pattern ---")
for i in range(1, rows + 1):
    # Loop to print numbers from 1 up to the current row number (i)
    for j in range(1, i + 1):
        print(j, end="")  # end="" keeps the numbers on the same line
    print()  # Moves to the next line after finishing the row


# --- Step 3: Print the Reverse Pattern ---
print("\n--- Reverse Pattern ---")
# We start from the full number of rows and count backward down to 1
for i in range(rows, 0, -1):
    # Loop to print numbers from 1 up to the current row size (i)
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Moves to the next line after finishing the row