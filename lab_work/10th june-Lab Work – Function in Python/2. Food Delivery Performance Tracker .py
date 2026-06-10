# 2. Food Delivery Performance Tracker 
# Problem Statement 
# Delivery times (in minutes) for different orders are given below: 
# delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
# Requirements 
# Create the following functions: 
# 1. fastest_delivery(times) 
# Returns the shortest delivery time. 
# 2. delayed_orders(times) 
# Returns a list of orders taking more than 45 minutes. 
# 3. average_delivery_time(times) 
# Returns the average delivery time. 
# 4. delivery_category(times) 
# Displays order categories: 
# • Fast → ≤ 30 minutes  
# • Normal → 31–45 minutes  
# • Delayed → > 45 minutes  
# Sample Output 
# Fastest Delivery: 18 minutes 
 
# Delayed Orders: 
# [60, 80, 55] 
 
# Average Delivery Time: 
# 40.8 minutes 
 
# Categories: 
# 28 -> Fast 
# 45 -> Normal 
# 60 -> Delayed 
# ...


# =====================================================================
# 2. Food Delivery Performance Tracker
# =====================================================================

# Our initial array list of order delivery times in minutes
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# 1. Function to find the shortest (minimum) delivery time
def fastest_delivery(times):
    # Set the first element as the initial minimum benchmark baseline
    shortest = times[0]
    
    # Loop through the list to find any value smaller than our current minimum
    for current_time in times:
        if current_time < shortest:
            shortest = current_time
            
    return shortest


# 2. Function to collect and return all orders taking more than 45 minutes
def delayed_orders(times):
    delayed_list = []
    
    # Loop and append to our tracking array if the order exceeds 45 minutes
    for current_time in times:
        if current_time > 45:
            delayed_list.append(current_time)
            
    return delayed_list


# 3. Function to calculate the average delivery time of all entries
def average_delivery_time(times):
    total_time = 0
    count = 0
    
    # Sum up all minutes and count the total number of orders manually
    for current_time in times:
        total_time += current_time
        count += 1
        
    # Prevent a division-by-zero error if the list is empty
    if count == 0:
        return 0.0
        
    return total_time / count


# 4. Function to categorize and display each delivery time line-by-line
def delivery_category(times):
    print("Categories:")
    
    for current_time in times:
        # Check against the specified threshold conditions
        if current_time <= 30:
            category = "Fast"
        elif current_time <= 45:
            category = "Normal"
        else:
            category = "Delayed"
            
        print(f"{current_time} -> {category}")


# =====================================================================
# Execution / Testing Program Block
# =====================================================================

# 1. Get and display the speed champion order
fastest = fastest_delivery(delivery_time)
print(f"Fastest Delivery: {fastest} minutes")
print()

# 2. Get and display the list of bottleneck late orders
delayed = delayed_orders(delivery_time)
print("Delayed Orders:")
print(delayed)
print()

# 3. Calculate and print the general logistics average speed metric
avg_time = average_delivery_time(delivery_time)
print("Average Delivery Time:")
print(f"{avg_time:.1f} minutes")
print()

# 4. Run the classification layout printing loop
delivery_category(delivery_time)