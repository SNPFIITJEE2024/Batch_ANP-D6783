# ==========================================
# 3. City Temperature Monitoring System
# ==========================================

# Initializing daily temperature data for different cities
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 

# ------------------------------------------
# Task 1: Display cities having temperature above 40°C.
# ------------------------------------------
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
print() # Layout spacing


# ------------------------------------------
# Task 2 & 3: Find the hottest and coolest city.
# ------------------------------------------
# Initialize tracking variables using the very first record in the dictionary
first_city = list(temperature.keys())[0]
first_temp = temperature[first_city]

hottest_city = first_city
max_temp = first_temp

coolest_city = first_city
min_temp = first_temp

# Loop to dynamically evaluate the temperature extreme boundaries
for city, temp in temperature.items():
    # Tracking extreme high boundary
    if temp > max_temp:
        max_temp = temp
        hottest_city = city
        
    # Tracking extreme low boundary
    if temp < min_temp:
        min_temp = temp
        coolest_city = city

print(f"Hottest City: {hottest_city} ({max_temp}°C)\n")
print(f"Coolest City: {coolest_city} ({min_temp}°C)\n")


# ------------------------------------------
# Task 4: Calculate average temperature.
# ------------------------------------------
total_temp = 0
total_cities = len(temperature)

for temp in temperature.values():
    total_temp += temp

# Finding the arithmetic mean
avg_temp = total_temp / total_cities
print(f"Average Temperature: {avg_temp:.1f}°C\n")


# ------------------------------------------
# Task 5: Create a list of pleasant cities (temperature < 35°C).
# ------------------------------------------
pleasant_cities = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:")
print(pleasant_cities)
print()


# ------------------------------------------
# Task 6: Count cities with temperature between 35°C and 40°C (inclusive).
# ------------------------------------------
mid_range_count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        mid_range_count += 1

print(f"Cities Between 35°C and 40°C: {mid_range_count}")