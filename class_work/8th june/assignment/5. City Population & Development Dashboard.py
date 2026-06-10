# 5. City Population & Development Dashboard 
# Problem Statement 
# The government wants to analyze city data. 
# Store details of at least 30 cities. 
# Example Structure 
# cities = { 
#     "Delhi": { 
#         "population": 32000000, 
#         "area": 1484, 
#         "literacy": 89 
#     } 
# } 
# Requirements 
# 1. Display all city details.  
# 2. Find the most populated city.  
# 3. Find the least populated city.  
# 4. Calculate average population.  
# 5. Display cities with literacy rate above 90%.  
# 6. Display cities with literacy below average.  
# 7. Calculate population density.  
# 8. Find city with highest density.  
# 9. Categorize cities:  
# o Small  
# o Medium  
# o Large  
# 10. Create a development-priority list.  
# 11. Generate separate dictionaries for:  
# o High Literacy Cities  
# o Low Literacy Cities  
# 12. Generate a national summary report.  
# Challenge 
# Rank all cities based on population density.


# # =====================================================================
# # City Population & Development Dashboard
# # =====================================================================

# # Initialize the nested dictionary with 30 diverse city profiles
# cities = {
#     "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
#     "Mumbai": {"population": 21000000, "area": 603, "literacy": 90},
#     "Bangalore": {"population": 13000000, "area": 741, "literacy": 92},
#     "Hyderabad": {"population": 10500000, "area": 650, "literacy": 85},
#     "Chennai": {"population": 9000000, "area": 426, "literacy": 91},
#     "Kolkata": {"population": 15000000, "area": 205, "literacy": 87},
#     "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 89},
#     "Pune": {"population": 7000000, "area": 331, "literacy": 93},
#     "Surat": {"population": 7500000, "area": 462, "literacy": 86},
#     "Jaipur": {"population": 4000000, "area": 484, "literacy": 83},
#     "Lucknow": {"population": 3800000, "area": 349, "literacy": 84},
#     "Kanpur": {"population": 3200000, "area": 260, "literacy": 82},
#     "Nagpur": {"population": 2900000, "area": 228, "literacy": 91},
#     "Indore": {"population": 3300000, "area": 276, "literacy": 88},
#     "Thane": {"population": 2500000, "area": 147, "literacy": 92},
#     "Bhopal": {"population": 2600000, "area": 285, "literacy": 87},
#     "Visakhapatnam": {"population": 2300000, "area": 540, "literacy": 82},
#     "Pimpri-Chinchwad": {"population": 2100000, "area": 181, "literacy": 90},
#     "Patna": {"population": 2400000, "area": 135, "literacy": 84},
#     "Vadodara": {"population": 1900000, "area": 220, "literacy": 91},
#     "Ghaziabad": {"population": 2400000, "area": 210, "literacy": 85},
#     "Ludhiana": {"population": 1700000, "area": 159, "literacy": 86},
#     "Agra": {"population": 1600000, "area": 121, "literacy": 75},
#     "Nashik": {"population": 1500000, "area": 259, "literacy": 90},
#     "Faridabad": {"population": 1400000, "area": 204, "literacy": 84},
#     "Meerut": {"population": 1300000, "area": 141, "literacy": 78},
#     "Rajkot": {"population": 1400000, "area": 170, "literacy": 88},
#     "Kalyan-Dombivli": {"population": 1200000, "area": 137, "literacy": 93},
#     "Vasai-Virar": {"population": 1200000, "area": 311, "literacy": 89},
#     "Varanasi": {"population": 1200000, "area": 82, "literacy": 77}
# }

# # 1. Display all city details
# def display_all_cities():
#     print(f"\n{'City Name':<18}{'Population':<15}{'Area (sq km)':<15}{'Literacy (%)':<10}")
#     print("-" * 60)
#     for name, data in cities.items():
#         print(f"{name:<18}{data['population']:<15}{data['area']:<15}{data['literacy']:<10}")

# # 2. Find the most populated city
# def get_most_populated():
#     name = max(cities, key=lambda k: cities[k]['population'])
#     return name, cities[name]['population']

# # 3. Find the least populated city
# def get_least_populated():
#     name = min(cities, key=lambda k: cities[k]['population'])
#     return name, cities[name]['population']

# # 4. Calculate average population across all tracked cities
# def calculate_average_population():
#     total_pop = sum(data['population'] for data in cities.values())
#     return total_pop / len(cities)

# # 5. Display cities with literacy rate above 90%
# def display_elite_literacy_cities():
#     print("\n--- Highly Literate Urban Centers (Literacy > 90%) ---")
#     for name, data in cities.items():
#         if data['literacy'] > 90:
#             print(f" ✨ {name:<18} | Literacy: {data['literacy']}%")

# # 6. Display cities with literacy below average
# def display_below_average_literacy():
#     total_lit = sum(data['literacy'] for data in cities.values())
#     avg_lit = total_lit / len(cities)
#     print(f"\n--- Cities with Literacy Below Average ({avg_lit:.1f}%) ---")
#     for name, data in cities.items():
#         if data['literacy'] < avg_lit:
#             print(f" ⚠️ {name:<18} | Literacy: {data['literacy']}%")

# # 7. Helper function to calculate population density (Population / Area)
# def get_density(city_name):
#     pop = cities[city_name]['population']
#     area = cities[city_name]['area']
#     return pop / area

# # 8. Find city with highest population density
# def get_highest_density_city():
#     name = max(cities, key=get_density)
#     return name, get_density(name)

# # 9. Categorize cities based on structural scale rules
# def display_scale_categories():
#     print("\n--- Demographic Scale Classifications ---")
#     for name, data in cities.items():
#         pop = data['population']
#         if pop >= 10000000:
#             scale = "Large (Megacity)"
#         elif pop >= 3000000:
#             scale = "Medium (Metropolis)"
#         else:
#             scale = "Small (Tier-2 Urban)"
#         print(f"🏙️ {name:<18} : {scale}")

# # 10. Create a development-priority list (Priority if literacy < 85% OR density > 10,000 per sq km)
# def generate_development_priority_list():
#     print("\n⚠️ ========= MUNICIPAL DEVELOPMENT PRIORITY LIST =========")
#     priority_list = []
#     for name, data in cities.items():
#         density = get_density(name)
#         # Target criteria setup rules
#         if data['literacy'] < 85 or density > 10000:
#             priority_list.append(name)
#             print(f"🚨 ALERT -> {name:<18} [Reason: Lit={data['literacy']}%, Density={density:.0f}/sq km]")
#     return priority_list

# # 11. Generate separate filtered split dictionaries for literacy metrics
# def split_cities_by_literacy():
#     high_lit_dict = {name: data for name, data in cities.items() if data['literacy'] >= 88}
#     low_lit_dict = {name: data for name, data in cities.items() if data['literacy'] < 88}
#     return high_lit_dict, low_lit_dict

# # 12. Generate a national summary report
# def print_national_summary_report():
#     print("\n" + "="*60)
#     print("                  NATIONAL URBAN METRIC SUMMARY REPORT          ")
#     print("="*60)
    
#     total_population = sum(d['population'] for d in cities.values())
#     total_area = sum(d['area'] for d in cities.values())
#     avg_population = calculate_average_population()
    
#     max_pop_name, max_pop_val = get_most_populated()
#     min_pop_name, min_pop_val = get_least_populated()
#     dense_name, dense_val = get_highest_density_city()
    
#     print(f"📊 Evaluated National Domain Population  : {total_population:,} citizens")
#     print(f"🗺️ Total Evaluated Municipal Landmass    : {total_area:,} sq km")
#     print(f"📈 General Mathematical Pop Average      : {avg_population:,.0f} per city")
#     print("-" * 60)
#     print(f"👑 Highest Concentrated Megacity        : {max_pop_name} ({max_pop_val:,})")
#     print(f"📉 Lowest Concentrated Entry            : {min_pop_name} ({min_pop_val:,})")
#     print(f"🔥 Most Constrained Infrastructure Area  : {dense_name} ({dense_val:.0f} people/sq km)")
#     print("="*60)


# # =====================================================================
# # Challenge: Rank all cities based on population density
# # =====================================================================
# def display_density_rankings():
#     print("\n" + "🌟" * 15)
#     print("   OFFICIAL DENSITY LEADERSHIP LEAGUE   ")
#     print("🌟" * 15)
    
#     # Sort the dictionary mapping items using our density calculator logic sequence
#     ranked_list = sorted(cities.keys(), key=get_density, reverse=True)
    
#     print(f"{'Rank':<6}{'City Name':<18}{'Density (per sq km)':<20}")
#     print("-" * 45)
#     for rank, name in enumerate(ranked_list, start=1):
#         density_val = get_density(name)
#         print(f"#{rank:<5}{name:<18}{density_val:<20.2f}")
#     print("-" * 45)


# # =====================================================================
# # Main Execution Module
# # =====================================================================

# # Display initial data grid
# display_all_cities()

# # Filter lookups execution
# display_elite_literacy_cities()
# display_below_average_literacy()

# # Run classification matrix loops
# display_scale_categories()
# priority_tracker = generate_development_priority_list()

# # Extract the high/low independent working maps
# high_lit_map, low_lit_map = split_cities_by_literacy()

# # Execute complete national overview compilation
# print_national_summary_report()

# # Run the final layout density ranking leaderboard challenge
# display_density_rankings()


# =====================================================================
# 5. City Population & Development Dashboard (Menu-Driven)
# =====================================================================

cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 90},
    "Bangalore": {"population": 13000000, "area": 741, "literacy": 92},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 85},
    "Chennai": {"population": 9000000, "area": 426, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 87},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 89},
    "Pune": {"population": 7000000, "area": 331, "literacy": 93},
    "Surat": {"population": 7500000, "area": 462, "literacy": 86},
    "Jaipur": {"population": 4000000, "area": 484, "literacy": 83},
    "Lucknow": {"population": 3800000, "area": 349, "literacy": 84},
    "Kanpur": {"population": 3200000, "area": 260, "literacy": 82},
    "Nagpur": {"population": 2900000, "area": 228, "literacy": 91},
    "Indore": {"population": 3300000, "area": 276, "literacy": 88},
    "Thane": {"population": 2500000, "area": 147, "literacy": 92},
    "Bhopal": {"population": 2600000, "area": 285, "literacy": 87},
    "Visakhapatnam": {"population": 2300000, "area": 540, "literacy": 82},
    "Pimpri-Chinchwad": {"population": 2100000, "area": 181, "literacy": 90},
    "Patna": {"population": 2400000, "area": 135, "literacy": 84},
    "Vadodara": {"population": 1900000, "area": 220, "literacy": 91},
    "Ghaziabad": {"population": 2400000, "area": 210, "literacy": 85},
    "Ludhiana": {"population": 1700000, "area": 159, "literacy": 86},
    "Agra": {"population": 1600000, "area": 121, "literacy": 75},
    "Nashik": {"population": 1500000, "area": 259, "literacy": 90},
    "Faridabad": {"population": 1400000, "area": 204, "literacy": 84},
    "Meerut": {"population": 1300000, "area": 141, "literacy": 78},
    "Rajkot": {"population": 1400000, "area": 170, "literacy": 88},
    "Kalyan-Dombivli": {"population": 1200000, "area": 137, "literacy": 93},
    "Vasai-Virar": {"population": 1200000, "area": 311, "literacy": 89},
    "Varanasi": {"population": 1200000, "area": 82, "literacy": 77}
}

while True:
    print("\n=========================================")
    print("      MUNICIPAL POPULATION TOOLSET MENU  ")
    print("=========================================")
    print("1. Display All City Profiles")
    print("2. Find Most Populated City")
    print("3. Find Least Populated City")
    print("4. Calculate Average Regional Population")
    print("5. View Literacy Elite Cities (> 90%)")
    print("6. View Below Average Literacy Outliers")
    print("7. Calculate and Show Densities Across Board")
    print("8. Identify Highest Population Density Anchor")
    print("9. Group and Categorize Cities by Scale Sizes")
    print("10. Print Development Priority Watch Lists")
    print("11. Extract Split Literacy Working Dictionaries")
    print("12. Print National Operations Summary Report")
    print("13. Challenge: Run Density Ranking Leaderboards")
    print("14. System Shutdown")
    print("=========================================")
    
    choice = input("Enter your choice (1-14): ")
    
    if choice == "1":
        print(f"\n{ 'City Name':<18 }{ 'Population':<15 }{ 'Area (sq km)':<15 }{ 'Literacy (%)':<10 }")
        print("-" * 60)
        for name, d in cities.items():
            print(f"{ name:<18 }{ d['population']:<15 }{ d['area']:<15 }{ d['literacy']:<10 }")
            
    elif choice == "2":
        high = None
        for name, d in cities.items():
            if high is None or d['population'] > cities[high]['population']:
                high = name
        print(f"\n👑 Most Populated Center: {high} ({cities[high]['population']:,} residents)")
        
    elif choice == "3":
        low = None
        for name, d in cities.items():
            if low is None or d['population'] < cities[low]['population']:
                low = name
        print(f"\n📉 Least Populated Center: {low} ({cities[low]['population']:,} residents)")
        
    elif choice == "4":
        tot_pop = 0
        cnt = 0
        for d in cities.values():
            tot_pop += d['population']
            cnt += 1
        print(f"\n📈 Mathematical Population Average: {tot_pop/cnt:,.0f} per city unit space")
        
    elif choice == "5":
        print("\n--- High Literacy Urban Anchors (>90%) ---")
        for name, d in cities.items():
            if d['literacy'] > 90:
                print(f"  ✨ {name:<18} | Literacy: {d['literacy']}%")
                
    elif choice == "6":
        tot_lit = 0
        cnt = 0
        for d in cities.values():
            tot_lit += d['literacy']
            cnt += 1
        avg_lit = tot_lit / cnt
        
        print(f"\n--- Literacy Deficit Centers (Below Average: {avg_lit:.1f}%) ---")
        for name, d in cities.items():
            if d['literacy'] < avg_lit:
                print(f"  ⚠️ {name:<18} | Literacy: {d['literacy']}%")
                
    elif choice == "7":
        print(f"\n{ 'City Name':<18 }{ 'Density (Per Sq Km)':<20 }")
        print("-" * 40)
        for name, d in cities.items():
            density = d['population'] / d['area']
            print(f" 🏙️ {name:<18} | {density:.2f} people/km²")
            
    elif choice == "8":
        dense_anchor = None
        for name, d in cities.items():
            current_density = d['population'] / d['area']
            if dense_anchor is None:
                dense_anchor = name
            else:
                max_density = cities[dense_anchor]['population'] / cities[dense_anchor]['area']
                if current_density > max_density:
                    dense_anchor = name
        final_density = cities[dense_anchor]['population'] / cities[dense_anchor]['area']
        print(f"\n🔥 Most Constrained Infrastructure: {dense_anchor} ({final_density:.2f} people/sq km)")
        
    elif choice == "9":
        print("\n--- Demographics Classification Matrix ---")
        for name, d in cities.items():
            p = d['population']
            if p >= 10000000: scale = "Large (Megacity)"
            elif p >= 3000000: scale = "Medium (Metropolis)"
            else: scale = "Small (Tier-2 Space)"
            print(f" 📦 {name:<18} : {scale}")
            
    elif choice == "10":
        print("\n⚠️ === INFRASTRUCTURE ACTION PRIORITY TRACK LINE ===")
        for name, d in cities.items():
            dens = d['population'] / d['area']
            if d['literacy'] < 85 or dens > 10000:
                print(f" 🚨 PRIORITY CALL -> {name:<15} [Lit: {d['literacy']}%, Density: {dens:.0f}/sq km]")
                
    elif choice == "11":
        high_literacy_map = {}
        low_literacy_map = {}
        for name, d in cities.items():
            if d['literacy'] >= 88:
                high_literacy_map[name] = {"lit": d['literacy']}
            else:
                low_literacy_map[name] = {"lit": d['literacy']}
        print("\n[System Split Complete] High literacy map generated with", len(high_literacy_map), "cities.")
        print("Low literacy map generated with", len(low_literacy_map), "cities.")
        
    elif choice == "12":
        tot_p = 0
        tot_a = 0
        for d in cities.values():
            tot_p += d['population']
            tot_a += d['area']
        print("\n" + "="*50)
        print("          NATIONAL LEVEL DOMAIN REPORT            ")
        print("="*50)
        print(f" Combined Domain Population : {tot_p:,} citizens")
        print(f" Tracked Managed Landmass   : {tot_a:,} sq km")
        print("="*50)
        
    elif choice == "13":
        # Create a mutable list layer tracking calculated values manually
        ranking_array = []
        for name, d in cities.items():
            density_val = d['population'] / d['area']
            ranking_array.append([name, density_val])
            
        # Implementing a pure custom descending Bubble Sort algorithm
        n = len(ranking_array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if ranking_array[j][1] < ranking_array[j + 1][1]:
                    ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
                    
        print("\n📊 --- COMPLETE SYSTEM MASTER DENSITY RANKING SHEET ---")
        print(f"{'Rank':<6}{'City Name':<18}{'Density (per sq km)':<20}")
        print("-" * 45)
        for rank in range(len(ranking_array)):
            print(f" #{rank+1:<5}{ranking_array[rank][0]:<18}{ranking_array[rank][1]:<20.2f}")
            
    elif choice == "14":
        break