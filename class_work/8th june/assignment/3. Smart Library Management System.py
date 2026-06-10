# 3. Smart Library Management System 
# Problem Statement 
# Create a digital library management system. 
# Example Structure 
# library = { 
#     "B101": { 
#         "title": "Python Basics", 
#         "author": "ABC", 
#         "copies": 5 
#     } 
# } 
# Maintain records of at least 30 books. 
# Requirements 
# 1. Add a book.  
# 2. Remove a book.  
# 3. Search a book by ID.  
# 4. Search by title.  
# 5. Update available copies.  
# 6. Issue a book.  
# 7. Return a book.  
# 8. Display books with fewer than 3 copies.  
# 9. Display books that are unavailable.  
# 10. Find the most available book.  
# 11. Generate a restocking report.  
# 12. Create a separate dictionary of books requiring immediate purchase.  
# Challenge 
# Generate a complete library summary report.

# # =====================================================================
# # Smart Library Management System
# # =====================================================================

# # Initialize the library directory with 30 unique book records
# library = {
#     "B101": {"title": "Python Basics", "author": "John Doe", "copies": 5},
#     "B102": {"title": "Data Structures in C", "author": "Ellis Horowitz", "copies": 2},
#     "B103": {"title": "Introduction to Algorithms", "author": "Thomas Cormen", "copies": 0},
#     "B104": {"title": "Clean Code", "author": "Robert Martin", "copies": 8},
#     "B105": {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "copies": 1},
#     "B106": {"title": "Design Patterns", "author": "Erich Gamma", "copies": 4},
#     "B107": {"title": "Artificial Intelligence", "author": "Stuart Russell", "copies": 3},
#     "B108": {"title": "Computer Networking", "author": "James Kurose", "copies": 6},
#     "B109": {"title": "Operating System Concepts", "author": "Avi Silberschatz", "copies": 0},
#     "B110": {"title": "Database System Concepts", "author": "Abraham Silberschatz", "copies": 5},
#     "B111": {"title": "Learning Web Design", "author": "Jennifer Robbins", "copies": 12},
#     "B112": {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "copies": 2},
#     "B113": {"title": "Head First Design Patterns", "author": "Eric Freeman", "copies": 4},
#     "B114": {"title": "You Don't Know JS", "author": "Kyle Simpson", "copies": 1},
#     "B115": {"title": "Compilers: Principles & Tools", "author": "Alfred Aho", "copies": 0},
#     "B116": {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "copies": 7},
#     "B117": {"title": "Fluent Python", "author": "Luciano Ramalho", "copies": 3},
#     "B118": {"title": "Effective Java", "author": "Joshua Bloch", "copies": 5},
#     "B119": {"title": "Cracking the Coding Interview", "author": "Gayle McDowell", "copies": 2},
#     "B120": {"title": "The C++ Programming Language", "author": "Bjarne Stroustrup", "copies": 4},
#     "B121": {"title": "Python Machine Learning", "author": "Sebastian Raschka", "copies": 1},
#     "B122": {"title": "Deep Learning", "author": "Ian Goodfellow", "copies": 3},
#     "B123": {"title": "Programming Pearls", "author": "Jon Bentley", "copies": 6},
#     "B124": {"title": "Code Complete", "author": "Steve McConnell", "copies": 0},
#     "B125": {"title": "Refactoring", "author": "Martin Fowler", "copies": 4},
#     "B126": {"title": "The Mythical Man-Month", "author": "Fred Brooks", "copies": 2},
#     "B127": {"title": "Pattern Recognition", "author": "Christopher Bishop", "copies": 5},
#     "B128": {"title": "Linux Kernel Development", "author": "Robert Love", "copies": 1},
#     "B129": {"title": "SQL Performance Explained", "author": "Markus Winand", "copies": 8},
#     "B130": {"title": "Domain-Driven Design", "author": "Eric Evans", "copies": 3}
# }

# # 1. Add a book
# def add_book(bid, title, author, copies):
#     if bid in library:
#         print(f"\n[Error] Book ID {bid} already exists. Use update instead.")
#     else:
#         library[bid] = {"title": title, "author": author, "copies": copies}
#         print(f"\n[Success] Added '{title}' under ID {bid}.")

# # 2. Remove a book
# def remove_book(bid):
#     if bid in library:
#         removed = library.pop(bid)
#         print(f"\n[Success] Removed '{removed['title']}' from catalog database.")
#     else:
#         print(f"\n[Error] Book ID {bid} not found.")

# # 3. Search a book by ID
# def search_by_id(bid):
#     print(f"\n--- Searching for Book ID: {bid} ---")
#     if bid in library:
#         b = library[bid]
#         print(f"ID: {bid} | Title: {b['title']} | Author: {b['author']} | Available Copies: {b['copies']}")
#         return library[bid]
#     else:
#         print("Result: No book found matching that ID.")
#         return None

# # 4. Search by title (Case-insensitive matching)
# def search_by_title(search_title):
#     print(f"\n--- Searching for Title: '{search_title}' ---")
#     found = False
#     for bid, details in library.items():
#         if search_title.lower() in details['title'].lower():
#             print(f"Found Match -> [{bid}] {details['title']} by {details['author']} ({details['copies']} left)")
#             found = True
#     if not found:
#         print("Result: No books match that title query.")

# # 5. Update available copies directly
# def update_copies(bid, new_copy_count):
#     if bid in library:
#         library[bid]['copies'] = new_copy_count
#         print(f"\n[Update] Adjusted '{library[bid]['title']}' stock level to {new_copy_count} copies.")
#     else:
#         print(f"\n[Error] Book ID {bid} not found.")

# # 6. Issue a book (Reduces copy count by 1)
# def issue_book(bid):
#     if bid in library:
#         if library[bid]['copies'] > 0:
#             library[bid]['copies'] -= 1
#             print(f"\n[Transaction] Issued '{library[bid]['title']}' successfully. Enjoy reading!")
#         else:
#             print(f"\n[Denied] '{library[bid]['title']}' is currently out of stock.")
#     else:
#         print(f"\n[Error] Book ID {bid} not registered.")

# # 7. Return a book (Increases copy count by 1)
# def return_book(bid):
#     if bid in library:
#         library[bid]['copies'] += 1
#         print(f"\n[Transaction] Checked in '{library[bid]['title']}'. Stock counter incremented.")
#     else:
#         print(f"\n[Error] This book ID doesn't belong to our catalog registry.")

# # 8. Find books with fewer than 3 copies
# def get_low_stock_books():
#     return {bid: details for bid, details in library.items() if 0 < details['copies'] < 3}

# # 9. Find books that are completely unavailable (copies == 0)
# def get_unavailable_books():
#     return {bid: details for bid, details in library.items() if details['copies'] == 0}

# # 10. Find the most available book (Maximum copy count)
# def get_most_available_book():
#     bid = max(library, key=lambda k: library[k]['copies'])
#     return bid, library[bid]

# # 11. Generate a restocking report
# def generate_restocking_report():
#     print("\n========= SYSTEM RESTOCKING OPERATION SHEETS =========")
#     unavailable = get_unavailable_books()
#     low_stock = get_low_stock_books()
    
#     print("\n🚨 EMPTY SHELVES (0 Copies Available):")
#     for bid, b in unavailable.items():
#         print(f" - [{bid}] '{b['title']}' by {b['author']}")
        
#     print("\n⚠️ ALERT: RUNNING LOW (Fewer than 3 copies remaining):")
#     for bid, b in low_stock.items():
#         print(f" - [{bid}] '{b['title']}' (Current Copies: {b['copies']})")

# # 12. Create a separate dictionary of books requiring immediate purchase (copies == 0)
# def get_immediate_purchase_dict():
#     # Explicit condition extraction mapping
#     return {bid: details for bid, details in library.items() if details['copies'] == 0}


# # =====================================================================
# # Challenge: Complete Library Summary Report
# # =====================================================================
# def print_library_summary_report():
#     print("\n" + "="*65)
#     print("                 SMART LIBRARY INFRASTRUCTURE SUMMARY          ")
#     print("="*65)
    
#     total_titles = len(library)
#     total_physical_books = sum(b['copies'] for b in library.values())
#     out_of_stock_count = len(get_unavailable_books())
#     low_stock_count = len(get_low_stock_books())
    
#     print(f"📚 Total Distinct Titles Cataloged : {total_titles}")
#     print(f"📖 Total Physical Units in House   : {total_physical_books} copies")
#     print(f"🛑 Out-of-Stock Status Items       : {out_of_stock_count} titles empty")
#     print(f"⚠️ Warning Flagged Low Stocks      : {low_stock_count} titles critical (< 3)")
    
#     # Showcase top tracking entity
#     most_avail_id, most_avail_details = get_most_available_book()
#     print(f"📈 Highest Volume Resource         : '{most_avail_details['title']}' ({most_avail_id}) with {most_avail_details['copies']} available units")
#     print("="*65)


# # =====================================================================
# # Main Code Execution / Testing Terminal 
# # =====================================================================

# # Add a brand new index book
# add_book("B131", "Learning ServiceNow and Workflows", "Tanuj Bhawariya", 10)

# # Simulate user desk check-out actions
# issue_book("B102")  # Lowering stock of 'Data Structures in C' from 2 down to 1
# issue_book("B103")  # Denied check-out on an unavailable title fallback test

# # Simulate user text search criteria strings
# search_by_title("python")
# search_by_id("B105")

# # Return workflow test
# return_book("B103")  # Checking back in an empty book slots it back to active level 1

# # Generate administrative reorder data extractions
# generate_restocking_report()

# # Spin off the secondary collection mapping structure required by management
# immediate_buy_list = get_immediate_purchase_dict()

# # Final report consolidation print out execution
# print_library_summary_report()


# =====================================================================
# 3. Smart Library Management System (Menu-Driven)
# =====================================================================

library = {
    "B101": {"title": "Python Basics", "author": "John Doe", "copies": 5},
    "B102": {"title": "Data Structures in C", "author": "Ellis Horowitz", "copies": 2},
    "B103": {"title": "Introduction to Algorithms", "author": "Thomas Cormen", "copies": 0},
    "B104": {"title": "Clean Code", "author": "Robert Martin", "copies": 8},
    "B105": {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "copies": 1},
    "B106": {"title": "Design Patterns", "author": "Erich Gamma", "copies": 4},
    "B107": {"title": "Artificial Intelligence", "author": "Stuart Russell", "copies": 3},
    "B108": {"title": "Computer Networking", "author": "James Kurose", "copies": 6},
    "B109": {"title": "Operating System Concepts", "author": "Avi Silberschatz", "copies": 0},
    "B110": {"title": "Database System Concepts", "author": "Abraham Silberschatz", "copies": 5},
    "B111": {"title": "Learning Web Design", "author": "Jennifer Robbins", "copies": 12},
    "B112": {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "copies": 2},
    "B113": {"title": "Head First Design Patterns", "author": "Eric Freeman", "copies": 4},
    "B114": {"title": "You Don't Know JS", "author": "Kyle Simpson", "copies": 1},
    "B115": {"title": "Compilers: Principles & Tools", "author": "Alfred Aho", "copies": 0},
    "B116": {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "copies": 7},
    "B117": {"title": "Fluent Python", "author": "Luciano Ramalho", "copies": 3},
    "B118": {"title": "Effective Java", "author": "Joshua Bloch", "copies": 5},
    "B119": {"title": "Cracking the Coding Interview", "author": "Gayle McDowell", "copies": 2},
    "B120": {"title": "The C++ Programming Language", "author": "Bjarne Stroustrup", "copies": 4},
    "B121": {"title": "Python Machine Learning", "author": "Sebastian Raschka", "copies": 1},
    "B122": {"title": "Deep Learning", "author": "Ian Goodfellow", "copies": 3},
    "B123": {"title": "Programming Pearls", "author": "Jon Bentley", "copies": 6},
    "B124": {"title": "Code Complete", "author": "Steve McConnell", "copies": 0},
    "B125": {"title": "Refactoring", "author": "Martin Fowler", "copies": 4},
    "B126": {"title": "The Mythical Man-Month", "author": "Fred Brooks", "copies": 2},
    "B127": {"title": "Pattern Recognition", "author": "Christopher Bishop", "copies": 5},
    "B128": {"title": "Linux Kernel Development", "author": "Robert Love", "copies": 1},
    "B129": {"title": "SQL Performance Explained", "author": "Markus Winand", "copies": 8},
    "B130": {"title": "Domain-Driven Design", "author": "Eric Evans", "copies": 3}
}

while True:
    print("\n=========================================")
    print("     SMART LIBRARY WORKSPACE SYSTEM      ")
    print("=========================================")
    print("1. Catalog New Book")
    print("2. Remove Book Profile Index")
    print("3. Query Book Metadata by ID")
    print("4. Pattern Search Books by Title")
    print("5. Overwrite Copy Stock Value Balance")
    print("6. Checkout/Issue Book Resource")
    print("7. Return/Check-in Book Resource")
    print("8. Display Endangered Stock Lists (< 3)")
    print("9. Display Blank Shelf Items (0 Copies)")
    print("10. Identify Maximum Available Stock Profile")
    print("11. Print Restocking Order Action Reports")
    print("12. Extract Immediate Procurement Dictionary")
    print("13. Print General Library Status Summary")
    print("14. System Shutdown")
    print("=========================================")
    
    choice = input("Enter your choice (1-14): ")
    
    if choice == "1":
        bid = input("Enter New Book Reference Key: ")
        if bid in library:
            print("\n[Error] System slot already occupied.")
        else:
            title = input("Book Title Name: ")
            author = input("Author Name: ")
            copies = int(input("Volume Quantities Logged: "))
            library[bid] = {"title": title, "author": author, "copies": copies}
            print(f"\n[Success] Item logged under index {bid}.")
            
    elif choice == "2":
        bid = input("Enter Book ID to scrub: ")
        if bid in library:
            deleted = library.pop(bid)
            print(f"\n[Scrubbed] Removed '{deleted['title']}' permanently.")
        else:
            print("\n[Error] Key reference index missing.")
            
    elif choice == "3":
        bid = input("Enter verification ID look up: ")
        if bid in library:
            print(f"\n[Match Found] -> Title: {library[bid]['title']} | Author: {library[bid]['author']} | In House: {library[bid]['copies']} units")
        else:
            print("\n[Error] Record slot empty.")
            
    elif choice == "4":
        query = input("Enter partial title string search criteria: ").lower()
        print("\n--- Filter Evaluation Scan Results ---")
        for bid, b in library.items():
            if query in b['title'].lower():
                print(f" 📑 [{bid}] {b['title']} - Author: {b['author']} ({b['copies']} left)")
                
    elif choice == "5":
        bid = input("Enter index target: ")
        if bid in library:
            cnt = int(input("Enter absolute system override count values: "))
            library[bid]['copies'] = cnt
            print("\n[Success] Storage metadata changed.")
        else:
            print("\n[Error] Index invalid.")
            
    elif choice == "6":
        bid = input("Enter Book ID requested for checkout: ")
        if bid in library:
            if library[bid]['copies'] > 0:
                library[bid]['copies'] -= 1
                print("\n[Approved] Counter ledger decremented. Dispatched asset.")
            else:
                print("\n[Rejected] Physical resource balance at zero levels.")
        else:
            print("\n[Error] Invalid Reference ID.")
            
    elif choice == "7":
        bid = input("Enter index identifier for check-in: ")
        if bid in library:
            library[bid]['copies'] += 1
            print("\n[Verified] Returned asset added to live inventory shelf loop.")
        else:
            print("\n[Warning] Asset mismatch. Registry track not located locally.")
            
    elif choice == "8":
        print("\n--- Warning Tracks: Low Volume Status (<3) ---")
        for bid, b in library.items():
            if 0 < b['copies'] < 3:
                print(f" ⚠️ '{b['title']}' ({bid}) | Only {b['copies']} volumes remaining")
                
    elif choice == "9":
        print("\n--- Empty Shelf Indexes ---")
        for bid, b in library.items():
            if b['copies'] == 0:
                print(f" ❌ [{bid}] {b['title']}")
                
    elif choice == "10":
        max_bid = None
        for bid, b in library.items():
            if max_bid is None or b['copies'] > library[max_bid]['copies']:
                max_bid = bid
        print(f"\n📦 Highest Volume Record Asset: '{library[max_bid]['title']}' ({max_bid}) - {library[max_bid]['copies']} units stack size.")
        
    elif choice == "11":
        print("\n=== SYSTEM LOGISTICS RESTOCK SHEET ===")
        for bid, b in library.items():
            if b['copies'] == 0:
                print(f"🚨 IMMEDIATE ACTION REQUIRED: '{b['title']}' ({bid}) has 0 copies.")
            elif b['copies'] < 3:
                print(f"⏳ MONITOR WARNING: '{b['title']}' ({bid}) has only {b['copies']} copies left.")
                
    elif choice == "12":
        procurement_dictionary = {}
        for bid, b in library.items():
            if b['copies'] == 0:
                procurement_dictionary[bid] = {"title": b['title'], "author": b['author']}
        print("\n[System] Procurement Object Generated:")
        print(procurement_dictionary)
        
    elif choice == "13":
        total_titles = 0
        total_units = 0
        empty_shelves = 0
        for b in library.values():
            total_titles += 1
            total_units += b['copies']
            if b['copies'] == 0:
                empty_shelves += 1
        print("\n" + "="*50)
        print("          CENTRAL ARCHIVE CORE SUMMARY            ")
        print("="*50)
        print(f" Total Cataloged Title Items : {total_titles} titles")
        print(f" Total Collective Unit Assets: {total_units} units")
        print(f" Unavailable Outage Channels : {empty_shelves} items")
        print("="*50)
        
    elif choice == "14":
        break