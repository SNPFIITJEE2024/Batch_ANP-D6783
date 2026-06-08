# Accept the total number of electricity units consumed from the user
units = int(input("Enter the total units consumed: "))

# Initialize the variable to calculate the total bill amount
total_bill = 0

# Calculate the bill based on slab rates
if units <= 100:
    # Everything falls into the first slab (₹5/unit)
    total_bill = units * 5
elif units <= 200:
    # First 100 units at ₹5/unit + remaining units at ₹7/unit
    total_bill = (100 * 5) + ((units - 100) * 7)
else:
    # First 100 units at ₹5 + next 100 units at ₹7 + anything remaining at ₹10/unit
    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Determine the consumption category based on units consumed
if units <= 100:
    category = "Low Consumption"
elif units <= 200:
    category = "Medium Consumption"
else:
    category = "High Consumption"

# Display the final summary output
print("\n--- Electricity Bill Summary ---")
print(f"Units Consumed : {units}")
print(f"Total Bill     : ₹{total_bill}")
print(f"Category       : {category}")