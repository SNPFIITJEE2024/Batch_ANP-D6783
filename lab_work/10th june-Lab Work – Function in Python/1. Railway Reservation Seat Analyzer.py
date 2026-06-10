# 1. Railway Reservation Seat Analyzer 
# Problem Statement 
# A railway coach has seats represented as follows: 
# seats = [ 
#     "Booked", "Available", "Booked", "Booked", 
#     "Available", "Available", "Booked", "Available", 
#     "Booked", "Booked", "Available", "Booked" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_seats(seats) 
# Returns the number of booked and available seats. 
# 2. first_available(seats) 
# Returns the seat number of the first available seat. 
# 3. occupancy_percentage(seats) 
# Returns the percentage of occupied seats. 
# 4. display_available_seats(seats) 
# Displays all available seat numbers. 
# Sample Output 
# Booked Seats: 7 
# Available Seats: 5 
 
# First Available Seat: 2 
 
# Occupancy Percentage: 58.33% 
 
# Available Seat Numbers: 
# 2 5 6 8 11


# =====================================================================
# 1. Railway Reservation Seat Analyzer
# =====================================================================

# Our initial coach seat mapping list
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
]

# 1. Function to count total booked and available seats
def count_seats(seat_list):
    booked_count = 0
    available_count = 0
    
    # Loop through each status in the list and increment counters
    for status in seat_list:
        if status == "Booked":
            booked_count += 1
        elif status == "Available":
            available_count += 1
            
    return booked_count, available_count


# 2. Function to find the seat number of the first available seat
def first_available(seat_list):
    # Loop using index values to track the position
    for index in range(len(seat_list)):
        if seat_list[index] == "Available":
            # Seat numbers start at 1, so we add 1 to our current index
            return index + 1
            
    return -1 # Returns -1 if the coach is completely full


# 3. Function to calculate the percentage of occupied (booked) seats
def occupancy_percentage(seat_list):
    total_seats = len(seat_list)
    
    # Fallback to prevent math errors if the list happens to be empty
    if total_seats == 0:
        return 0.0
        
    booked_count = 0
    for status in seat_list:
        if status == "Booked":
            booked_count += 1
            
    # Calculate percentage: (Part / Total) * 100
    percentage = (booked_count / total_seats) * 100
    return percentage


# 4. Function to display all available seat numbers line-by-line
def display_available_seats(seat_list):
    print("Available Seat Numbers:")
    
    for index in range(len(seat_list)):
        if seat_list[index] == "Available":
            # Add 1 to index to display human-readable passenger seat numbers
            print(index + 1, end=" ")
    print() # Prints a clean empty newline at the very end


# =====================================================================
# Execution / Testing Program Block
# =====================================================================

# Call our counting function and unpack the two returned values
total_booked, total_available = count_seats(seats)
print(f"Booked Seats: {total_booked}")
print(f"Available Seats: {total_available}")
print()

# Find and print the first empty window seat option
first_seat = first_available(seats)
print(f"First Available Seat: {first_seat}")
print()

# Get coach percentage capacity utilization rate format to 2 decimal points
occupied_ratio = occupancy_percentage(seats)
print(f"Occupancy Percentage: {occupied_ratio:.2%}")
print()

# Call display function to loop out remaining seat positions
display_available_seats(seats)