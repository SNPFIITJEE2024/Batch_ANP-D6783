# 2. E-Commerce Inventory & Sales Dashboard 
# Problem Statement 
# An online store wants to manage products and sales. 
# Example Structure 
# products = { 
#     "P101": { 
#         "name": "Laptop", 
#         "price": 55000, 
#         "stock": 12, 
#         "sold": 25 
#     } 
# } 
# Maintain records of at least 30 products. 
# Requirements 
# 1. Display all products.  
# 2. Add a new product.  
# 3. Update stock after sales.  
# 4. Find out-of-stock products.  
# 5. Find products with stock less than 5.  
# 6. Calculate total inventory value.  
# 7. Find best-selling product.  
# 8. Find least-selling product.  
# 9. Calculate total revenue generated.  
# 10. Generate a low-stock report.  
# 11. Display products whose sales exceed the average sales.  
# 12. Create a dictionary of products eligible for promotion (sales < 10).  
# Challenge 
# Generate a complete business report.


# # =====================================================================
# # E-Commerce Inventory & Sales Dashboard
# # =====================================================================

# # Initialize the nested dictionary with 30 unique products
# products = {
#     "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
#     "P102": {"name": "Smartphone", "price": 25000, "stock": 35, "sold": 80},
#     "P103": {"name": "Wireless Mouse", "price": 1200, "stock": 4, "sold": 120},
#     "P104": {"name": "Mechanical Keyboard", "price": 4500, "stock": 8, "sold": 45},
#     "P105": {"name": "Bluetooth Speaker", "price": 3500, "stock": 0, "sold": 60},
#     "P106": {"name": "Gaming Monitor", "price": 18000, "stock": 6, "sold": 18},
#     "P107": {"name": "External Hard Drive", "price": 5000, "stock": 15, "sold": 30},
#     "P108": {"name": "USB-C Hub", "price": 2200, "stock": 25, "sold": 95},
#     "P109": {"name": "Noise Cancelling Headphones", "price": 12000, "stock": 3, "sold": 40},
#     "P110": {"name": "Webcam 1080p", "price": 3800, "stock": 0, "sold": 55},
#     "P111": {"name": "Graphic Tablet", "price": 8500, "stock": 7, "sold": 14},
#     "P112": {"name": "Laptop Stand", "price": 1800, "stock": 40, "sold": 70},
#     "P113": {"name": "Desk Mat", "price": 900, "stock": 50, "sold": 110},
#     "P114": {"name": "Ring Light", "price": 1500, "stock": 18, "sold": 32},
#     "P115": {"name": "HDMI Cable 2m", "price": 450, "stock": 100, "sold": 250},
#     "P116": {"name": "Power Bank 20k", "price": 2500, "stock": 2, "sold": 85},
#     "P117": {"name": "Smart Watch", "price": 6000, "stock": 14, "sold": 50},
#     "P118": {"name": "SSD 1TB Internal", "price": 7500, "stock": 9, "sold": 22},
#     "P119": {"name": "CPU Cooler", "price": 3200, "stock": 5, "sold": 12},
#     "P120": {"name": "RAM DDR4 16GB", "price": 4200, "stock": 11, "sold": 38},
#     "P121": {"name": "Microphone Stand", "price": 1300, "stock": 22, "sold": 7},
#     "P122": {"name": "Pop Filter", "price": 400, "stock": 30, "sold": 45},
#     "P123": {"name": "LED Light Strip", "price": 800, "stock": 16, "sold": 130},
#     "P124": {"name": "Air Duster Spray", "price": 600, "stock": 0, "sold": 140},
#     "P125": {"name": "Thermal Paste", "price": 350, "stock": 65, "sold": 90},
#     "P126": {"name": "Wi-Fi Router Dongle", "price": 2800, "stock": 13, "sold": 4},
#     "P127": {"name": "Ergonomic Office Chair", "price": 14000, "stock": 4, "sold": 9},
#     "P128": {"name": "Laptop Sleeve Case", "price": 1100, "stock": 28, "sold": 62},
#     "P129": {"name": "Cable Management Clips", "price": 250, "stock": 120, "sold": 5},
#     "P130": {"name": "Screen Cleaning Kit", "price": 300, "stock": 45, "sold": 115}
# }

# # 1. Display all products
# def display_all_products():
#     print(f"\n{'PID':<7}{'Product Name':<30}{'Price':<10}{'Stock':<8}{'Sold':<6}")
#     print("-" * 65)
#     for pid, details in products.items():
#         print(f"{pid:<7}{details['name']:<30}{details['price']:<10}{details['stock']:<8}{details['sold']:<6}")

# # 2. Add a new product
# def add_product(pid, name, price, stock, sold=0):
#     if pid in products:
#         print(f"\n[Error] Product ID {pid} already exists.")
#     else:
#         products[pid] = {"name": name, "price": price, "stock": stock, "sold": sold}
#         print(f"\n[Success] Added new product: {name} ({pid})")

# # 3. Update stock after sales
# def record_sale(pid, quantity_sold):
#     if pid in products:
#         if products[pid]['stock'] >= quantity_sold:
#             products[pid]['stock'] -= quantity_sold
#             products[pid]['sold'] += quantity_sold
#             print(f"\n[Update] Sold {quantity_sold} units of {products[pid]['name']}.")
#         else:
#             print(f"\n[Error] Cannot sell {quantity_sold} units of {products[pid]['name']}. Only {products[pid]['stock']} in stock.")
#     else:
#         print(f"\n[Error] Product {pid} not found.")

# # 4. Find out-of-stock products (stock == 0)
# def get_out_of_stock():
#     return {pid: details for pid, details in products.items() if details['stock'] == 0}

# # 5. Find products with stock less than 5
# def get_critical_stock():
#     return {pid: details for pid, details in products.items() if 0 < details['stock'] < 5}

# # 6. Calculate total inventory value (stock * price)
# def calculate_total_inventory_value():
#     return sum(details['stock'] * details['price'] for details in products.values())

# # 7. Find best-selling product
# def get_best_seller():
#     pid = max(products, key=lambda k: products[k]['sold'])
#     return pid, products[pid]

# # 8. Find least-selling product
# def get_least_seller():
#     pid = min(products, key=lambda k: products[k]['sold'])
#     return pid, products[pid]

# # 9. Calculate total revenue generated (sold * price)
# def calculate_total_revenue():
#     return sum(details['sold'] * details['price'] for details in products.values())

# # 10. Generate a low-stock report
# def generate_low_stock_report():
#     print("\n========= LOW STOCK ACTION REPORT =========")
#     out_of_stock = get_out_of_stock()
#     critical_stock = get_critical_stock()
    
#     print("\n❌ CRITICAL: OUT OF STOCK (Needs Immediate Reorder)")
#     for pid, d in out_of_stock.items():
#         print(f" - [{pid}] {d['name']} (Total units sold to date: {d['sold']})")
        
#     print("\n⚠️ WARNING: LOW STOCK (Less than 5 units remaining)")
#     for pid, d in critical_stock.items():
#         print(f" - [{pid}] {d['name']} (Current Stock: {d['stock']})")

# # 11. Display products whose sales exceed the average sales
# def display_above_average_sales():
#     total_sales_count = sum(d['sold'] for d in products.values())
#     avg_sales = total_sales_count / len(products)
#     print(f"\n--- Products Exceeding Average Unit Sales ({avg_sales:.1f} units) ---")
#     for pid, d in products.items():
#         if d['sold'] > avg_sales:
#             print(f" - {d['name']:<30} (Sold: {d['sold']} units)")

# # 12. Create a dictionary of products eligible for promotion (sales < 10)
# def get_promo_eligible_products():
#     return {pid: d for pid, d in products.items() if d['sold'] < 10}


# # =====================================================================
# # Challenge: Complete Business Executive Report
# # =====================================================================
# def generate_complete_business_report():
#     print("\n" + "="*60)
#     print("             EXECUTIVE BUSINESS OPERATIONS REPORT             ")
#     print("="*60)
    
#     # Financial Stats
#     total_rev = calculate_total_revenue()
#     inv_value = calculate_total_inventory_value()
#     print(f"💵 Total Revenue Generated : ₹{total_rev:,}")
#     print(f"📦 Active Warehouse Value  : ₹{inv_value:,}")
    
#     # Sales Leaders
#     best_id, best_det = get_best_seller()
#     least_id, least_det = get_least_seller()
#     print(f"🔥 MVP Best Selling Item   : {best_det['name']} ({best_id}) - {best_det['sold']} units sold")
#     print(f"❄️ Slow Moving Product     : {least_det['name']} ({least_id}) - {least_det['sold']} units sold")
    
#     # Stock health count
#     out_count = len(get_out_of_stock())
#     low_count = len(get_critical_stock())
#     print(f"🚨 Inventory Health Alerts : {out_count} items out-of-stock | {low_count} items running low")
    
#     # Marketing Target Insight
#     promo_items = get_promo_eligible_products()
#     print(f"🎯 Marketing Campaign Target: {len(promo_items)} products flagged for promotion clearance (sales < 10 units)")
#     print("="*60)


# # =====================================================================
# # Testing Module / Code Execution
# # =====================================================================

# # Display initial status
# print("--- INITIAL PRODUCT INVENTORY CATALOG ---")
# display_all_products()

# # Add a brand new product to the matrix
# add_product("P131", "Wireless Charger Pad", 1500, 20, 0)

# # Record a live customer checkout sequence
# record_sale("P101", 2)  # Sell 2 laptops
# record_sale("P103", 2)  # Sell 2 wireless mice (leaves stock at 2)
# record_sale("P105", 5)  # Try to sell an out-of-stock speaker (Triggers error safely)

# # Run isolated administrative analysis functions
# generate_low_stock_report()
# display_above_average_sales()

# # Display the promotional structure extraction results
# promo_dictionary = get_promo_eligible_products()

# # Compile the final comprehensive warehouse dashboard summary
# generate_complete_business_report()


# =====================================================================
# 2. E-Commerce Inventory & Sales Dashboard (Menu-Driven)
# =====================================================================

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Smartphone", "price": 25000, "stock": 35, "sold": 80},
    "P103": {"name": "Wireless Mouse", "price": 1200, "stock": 4, "sold": 120},
    "P104": {"name": "Mechanical Keyboard", "price": 4500, "stock": 8, "sold": 45},
    "P105": {"name": "Bluetooth Speaker", "price": 3500, "stock": 0, "sold": 60},
    "P106": {"name": "Gaming Monitor", "price": 18000, "stock": 6, "sold": 18},
    "P107": {"name": "External Hard Drive", "price": 5000, "stock": 15, "sold": 30},
    "P108": {"name": "USB-C Hub", "price": 2200, "stock": 25, "sold": 95},
    "P109": {"name": "Noise Cancelling Headphones", "price": 12000, "stock": 3, "sold": 40},
    "P110": {"name": "Webcam 1080p", "price": 3800, "stock": 0, "sold": 55},
    "P111": {"name": "Graphic Tablet", "price": 8500, "stock": 7, "sold": 14},
    "P112": {"name": "Laptop Stand", "price": 1800, "stock": 40, "sold": 70},
    "P113": {"name": "Desk Mat", "price": 900, "stock": 50, "sold": 110},
    "P114": {"name": "Ring Light", "price": 1500, "stock": 18, "sold": 32},
    "P115": {"name": "HDMI Cable 2m", "price": 450, "stock": 100, "sold": 250},
    "P116": {"name": "Power Bank 20k", "price": 2500, "stock": 2, "sold": 85},
    "P117": {"name": "Smart Watch", "price": 6000, "stock": 14, "sold": 50},
    "P118": {"name": "SSD 1TB Internal", "price": 7500, "stock": 9, "sold": 22},
    "P119": {"name": "CPU Cooler", "price": 3200, "stock": 5, "sold": 12},
    "P120": {"name": "RAM DDR4 16GB", "price": 4200, "stock": 11, "sold": 38},
    "P121": {"name": "Microphone Stand", "price": 1300, "stock": 22, "sold": 7},
    "P122": {"name": "Pop Filter", "price": 400, "stock": 30, "sold": 45},
    "P123": {"name": "LED Light Strip", "price": 800, "stock": 16, "sold": 130},
    "P124": {"name": "Air Duster Spray", "price": 600, "stock": 0, "sold": 140},
    "P125": {"name": "Thermal Paste", "price": 350, "stock": 65, "sold": 90},
    "P126": {"name": "Wi-Fi Router Dongle", "price": 2800, "stock": 13, "sold": 4},
    "P127": {"name": "Ergonomic Office Chair", "price": 14000, "stock": 4, "sold": 9},
    "P128": {"name": "Laptop Sleeve Case", "price": 1100, "stock": 28, "sold": 62},
    "P129": {"name": "Cable Management Clips", "price": 250, "stock": 120, "sold": 5},
    "P130": {"name": "Screen Cleaning Kit", "price": 300, "stock": 45, "sold": 115}
}

while True:
    print("\n=========================================")
    print("     E-COMMERCE MANAGEMENT MENU          ")
    print("=========================================")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Record Product Sale (Deduct Stock)")
    print("4. View Out-of-Stock Products")
    print("5. View Critical Stock Items (< 5)")
    print("6. Calculate Total Asset Inventory Value")
    print("7. Identify Best & Least Selling Items")
    print("8. Check Total Revenue Generated")
    print("9. Generate Low-Stock Warning Report")
    print("10. Display Products Exceeding Average Unit Sales")
    print("11. Extract Promotion Eligible Pool (< 10 Sold)")
    print("12. Compile Executive Business Report")
    print("13. Exit")
    print("=========================================")
    
    choice = input("Enter your choice (1-13): ")
    
    if choice == "1":
        print(f"\n{ 'PID':<7 }{ 'Product Name':<30 }{ 'Price':<10 }{ 'Stock':<8 }{ 'Sold':<6 }")
        print("-" * 65)
        for pid, d in products.items():
            print(f"{ pid:<7 }{ d['name']:<30 }{ d['price']:<10 }{ d['stock']:<8 }{ d['sold']:<6 }")
            
    elif choice == "2":
        pid = input("Enter New Product ID: ")
        if pid in products:
            print("\n[Error] Product identifier already exists.")
        else:
            name = input("Product Name: ")
            price = int(input("Unit Price (INR): "))
            stock = int(input("Opening Stock Units: "))
            products[pid] = {"name": name, "price": price, "stock": stock, "sold": 0}
            print(f"\n[Success] Added {name} into warehouse database tracker.")
            
    elif choice == "3":
        pid = input("Enter Product ID sold: ")
        if pid in products:
            qty = int(input("Enter units quantity bought by customer: "))
            if products[pid]['stock'] >= qty:
                products[pid]['stock'] -= qty
                products[pid]['sold'] += qty
                print(f"\n[Update] Inventory stock lowered. {qty} units dispatched.")
            else:
                print(f"\n[Denied] Insufficient warehouse stock level. Total left: {products[pid]['stock']}")
        else:
            print("\n[Error] Product ID not recognized.")
            
    elif choice == "4":
        print("\n--- Out Of Stock Matrix List ---")
        for pid, d in products.items():
            if d['stock'] == 0:
                print(f"❌ {pid} | {d['name']}")
                
    elif choice == "5":
        print("\n--- Low Stock Watch List (<5) ---")
        for pid, d in products.items():
            if 0 < d['stock'] < 5:
                print(f"⚠️ {pid} | {d['name']} - Only {d['stock']} units left!")
                
    elif choice == "6":
        total_value = 0
        for d in products.values():
            total_value += (d['stock'] * d['price'])
        print(f"\n📦 Warehouse Stock Asset Valuation: INR {total_value:,}")
        
    elif choice == "7":
        best_pid = None
        least_pid = None
        for pid, d in products.items():
            if best_pid is None or d['sold'] > products[best_pid]['sold']:
                best_pid = pid
            if least_pid is None or d['sold'] < products[least_pid]['sold']:
                least_pid = pid
        print(f"\n🔥 Best Seller  : {products[best_pid]['name']} ({best_pid}) - {products[best_pid]['sold']} items sold")
        print(f"❄️ Least Seller : {products[least_pid]['name']} ({least_pid}) - {products[least_pid]['sold']} items sold")
        
    elif choice == "8":
        revenue = 0
        for d in products.values():
            revenue += (d['sold'] * d['price'])
        print(f"\n💵 Total Turn-over Gross Revenue: INR {revenue:,}")
        
    elif choice == "9":
        print("\n=== SYSTEM INVENTORY ACTION ALERTS ===")
        for pid, d in products.items():
            if d['stock'] == 0:
                print(f"🔥 CRITICAL REORDER -> {d['name']} ({pid}) is empty!")
            elif d['stock'] < 5:
                print(f"⚠️ WARNING WATCHLINE -> {d['name']} ({pid}) is running low: {d['stock']} left")
                
    elif choice == "10":
        total_sold = 0
        p_count = 0
        for d in products.values():
            total_sold += d['sold']
            p_count += 1
        avg_units = total_sold / p_count
        
        print(f"\n--- Moving Faster Than System Average ({avg_units:.1f} units) ---")
        for pid, d in products.items():
            if d['sold'] > avg_units:
                print(f" 📈 {d['name']:<30} | {d['sold']} items sold")
                
    elif choice == "11":
        clearance_promo = {}
        for pid, d in products.items():
            if d['sold'] < 10:
                clearance_promo[pid] = {"name": d['name'], "sold": d['sold']}
        print("\n[System] New Clearance Target Dictionary Output Created:")
        print(clearance_promo)
        
    elif choice == "12":
        rev = 0
        assets = 0
        best_p = None
        for pid, d in products.items():
            rev += (d['sold'] * d['price'])
            assets += (d['stock'] * d['price'])
            if best_p is None or d['sold'] > products[best_p]['sold']:
                best_p = pid
                
        print("\n" + "="*50)
        print("          EXECUTIVE PERFORMANCE REPORT            ")
        print("="*50)
        print(f" Gross Pipeline Revenue : INR {rev:,}")
        print(f" Live Tied Asset Capital : INR {assets:,}")
        print(f" Leading Marketplace Item: {products[best_p]['name']} ({best_p})")
        print("="*50)
        
    elif choice == "13":
        break