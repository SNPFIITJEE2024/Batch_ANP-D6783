# ==========================================
# 1. Online Shopping Order Analytics 
# ==========================================

# Initializing the product sales data dictionary
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 

#-------------------------------------------
# Task 1: Display products sold more than 20 times.
# ------------------------------------------
print("Products Sold More Than 20 Times:")
for product, count in sales.items():
    if count > 20:
        print(product)
print() # Printing an empty line for clean layout spacing


# ------------------------------------------
# Task 2 & 3: Find the best-selling and least-selling product.
# ------------------------------------------
# We initialize our trackers using the first item in the dictionary
first_product = list(sales.keys())[0]
first_value = sales[first_product]

best_product = first_product
max_sales = first_value

least_product = first_product
min_sales = first_value

# Loop through the dictionary to evaluate max and min boundaries
for product, count in sales.items():
    # Checking for the highest sales number
    if count > max_sales:
        max_sales = count
        best_product = product
        
    # Checking for the lowest sales number
    if count < min_sales:
        min_sales = count
        least_product = product

print(f"Best Selling Product: {best_product} ({max_sales})\n")
print(f"Least Selling Product: {least_product} ({min_sales})\n")


# ------------------------------------------
# Task 4: Calculate total products sold.
# ------------------------------------------
total_units = 0
for count in sales.values():
    total_units += count

print(f"Total Units Sold: {total_units}\n")


# ------------------------------------------
# Task 5: Create a list of products requiring promotion (sales < 15).
# ------------------------------------------
promo_list = []
for product, count in sales.items():
    if count < 15:
        promo_list.append(product)

print("Products Requiring Promotion:")
print(promo_list)
print()


# ------------------------------------------
# Task 6: Count products having sales between 10 and 30 (inclusive).
# ------------------------------------------
mid_range_count = 0
for count in sales.values():
    if 10 <= count <= 30:
        mid_range_count += 1

print(f"Products Having Sales Between 10 and 30: {mid_range_count}")# ==========================================
