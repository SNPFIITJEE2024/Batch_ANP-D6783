# ==========================================
# 5. Smart Electricity Billing System 
# ==========================================

# Initializing monthly electricity consumption data (in units)
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 

# ------------------------------------------
# Task 1: Display houses consuming more than 400 units.
# ------------------------------------------
print("Houses Consuming More Than 400 Units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)
print() # Layout spacing


# ------------------------------------------
# Task 2 & 3: Find the highest and lowest consuming houses.
# ------------------------------------------
# Establish baseline boundary checkpoints using the first item in the dictionary
first_house = list(units.keys())[0]
first_consumption = units[first_house]

highest_house = first_house
max_units = first_consumption

lowest_house = first_house
min_units = first_consumption

# Loop through the data to update extreme high and low benchmarks
for house, consumption in units.items():
    # Tracking highest consumption spike
    if consumption > max_units:
        max_units = consumption
        highest_house = house
        
    # Tracking lowest consumption baseline
    if consumption < min_units:
        min_units = consumption
        lowest_house = house

print("Highest Consumption:")
print(f"{highest_house} ({max_units} units)\n")

print("Lowest Consumption:")
print(f"{lowest_house} ({min_units} units)\n")


# ------------------------------------------
# Task 4: Calculate total units consumed across the grid.
# ------------------------------------------
total_units_consumed = 0
for consumption in units.values():
    total_units_consumed += consumption

print(f"Total Units Consumed: {total_units_consumed}\n")


# ------------------------------------------
# Task 5: Create and separate categorization lists based on usage profiles.
# ------------------------------------------
low_consumption = []
medium_consumption = []
high_consumption = []

for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif 200 <= consumption <= 400:
        medium_consumption.append(house)
    else: # This implicitly captures everything strictly > 400
        high_consumption.append(house)

print("Low Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)
print()


# ------------------------------------------
# Task 6: Count houses eligible for energy-saving campaign (consumption > 300).
# ------------------------------------------
campaign_eligible_count = 0
for consumption in units.values():
    if consumption > 300:
        campaign_eligible_count += 1

print(f"Eligible for Energy-Saving Campaign: {campaign_eligible_count}")