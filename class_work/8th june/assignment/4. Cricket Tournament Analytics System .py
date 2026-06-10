# 4. Cricket Tournament Analytics System 
# Problem Statement 
# Store statistics of at least 30 cricket players. 
# Example Structure 
# players = { 
#     "Virat": { 
#         "runs": 645, 
#         "matches": 12, 
#         "wickets": 0 
#     } 
# } 
# Requirements 
# 1. Display all player statistics.  
# 2. Find highest run scorer.  
# 3. Find lowest run scorer.  
# 4. Calculate average runs.  
# 5. Find player with maximum wickets.  
# 6. Find all-rounders (runs > 300 and wickets > 5).  
# 7. Display players scoring above average.  
# 8. Create categories:  
# o Star Performer  
# o Good Performer  
# o Average Performer  
# o Poor Performer  
# 9. Generate team statistics.  
# 10. Display top 5 batsmen.  
# 11. Display top 5 bowlers.  
# 12. Create a separate dictionary for award winners.  
# Challenge 
# Generate a tournament report.

# # =====================================================================
# # Cricket Tournament Analytics System
# # =====================================================================

# # Initialize the master nested dictionary with 30 cricket player records
# players = {
#     "Virat": {"runs": 645, "matches": 12, "wickets": 0},
#     "Rohit": {"runs": 510, "matches": 12, "wickets": 1},
#     "Rahul": {"runs": 380, "matches": 11, "wickets": 0},
#     "Hardik": {"runs": 340, "matches": 12, "wickets": 14},
#     "Jadeja": {"runs": 210, "matches": 12, "wickets": 18},
#     "Bumrah": {"runs": 25, "matches": 10, "wickets": 24},
#     "Shami": {"runs": 12, "matches": 9, "wickets": 21},
#     "Siraj": {"runs": 8, "matches": 11, "wickets": 12},
#     "Kuldeep": {"runs": 35, "matches": 10, "wickets": 15},
#     "Gill": {"runs": 480, "matches": 12, "wickets": 0},
#     "Iyer": {"runs": 410, "matches": 12, "wickets": 0},
#     "Pant": {"runs": 365, "matches": 10, "wickets": 0},
#     "Sky": {"runs": 290, "matches": 12, "wickets": 1},
#     "Axar": {"runs": 185, "matches": 9, "wickets": 11},
#     "Ashwin": {"runs": 120, "matches": 6, "wickets": 8},
#     "Thakur": {"runs": 95, "matches": 7, "wickets": 6},
#     "Chahal": {"runs": 5, "matches": 5, "wickets": 7},
#     "Sundar": {"runs": 110, "matches": 8, "wickets": 5},
#     "Dube": {"runs": 160, "matches": 8, "wickets": 3},
#     "Jaiswal": {"runs": 525, "matches": 12, "wickets": 0},
#     "Rinku": {"runs": 240, "matches": 10, "wickets": 0},
#     "Kishan": {"runs": 210, "matches": 6, "wickets": 0},
#     "Ruturaj": {"runs": 315, "matches": 8, "wickets": 0},
#     "Samson": {"runs": 190, "matches": 7, "wickets": 0},
#     "Arshdeep": {"runs": 18, "matches": 12, "wickets": 17},
#     "Mukesh": {"runs": 10, "matches": 6, "wickets": 5},
#     "Avesh": {"runs": 4, "matches": 4, "wickets": 4},
#     "Bishnoi": {"runs": 2, "matches": 5, "wickets": 6},
#     "Harshit": {"runs": 15, "matches": 3, "wickets": 4},
#     "Nitish": {"runs": 145, "matches": 5, "wickets": 4}
# }

# # 1. Display all player statistics
# def display_all_players():
#     print(f"\n{'Player Name':<15}{'Matches':<10}{'Runs':<10}{'Wickets':<10}")
#     print("-" * 45)
#     for name, stats in players.items():
#         print(f"{name:<15}{stats['matches']:<10}{stats['runs']:<10}{stats['wickets']:<10}")

# # 2. Find highest run scorer
# def get_orange_cap():
#     name = max(players, key=lambda k: players[k]['runs'])
#     return name, players[name]['runs']

# # 3. Find lowest run scorer
# def get_lowest_scorer():
#     name = min(players, key=lambda k: players[k]['runs'])
#     return name, players[name]['runs']

# # 4. Calculate average tournament runs per player
# def calculate_class_run_average():
#     total_runs = sum(stats['runs'] for stats in players.values())
#     return total_runs / len(players)

# # 5. Find player with maximum wickets
# def get_purple_cap():
#     name = max(players, key=lambda k: players[k]['wickets'])
#     return name, players[name]['wickets']

# # 6. Find all-rounders (runs > 300 and wickets > 5)
# def display_all_rounders():
#     print("\n--- Tournament All-Rounders (Runs > 300 & Wickets > 5) ---")
#     found = False
#     for name, stats in players.items():
#         if stats['runs'] > 300 and stats['wickets'] > 5:
#             print(f"🏏 {name} - Runs: {stats['runs']} | Wickets: {stats['wickets']}")
#             found = True
#     if not found:
#         print("No players met the criteria.")

# # 7. Display players scoring above average
# def display_above_average_batsmen():
#     avg_runs = calculate_class_run_average()
#     print(f"\n--- Batsmen Scoring Above Tournament Average ({avg_runs:.1f} runs) ---")
#     for name, stats in players.items():
#         if stats['runs'] > avg_runs:
#             print(f" - {name:<12} | Runs scored: {stats['runs']}")

# # 8. Categorize players based on performance criteria
# def show_player_performance_categories():
#     print("\n--- Player Tier Classification Sheets ---")
#     for name, stats in players.items():
#         r = stats['runs']
#         w = stats['wickets']
        
#         # Classification evaluation logic rules
#         if r >= 500 or w >= 20:
#             category = "Star Performer"
#         elif r >= 300 or w >= 12:
#             category = "Good Performer"
#         elif r >= 100 or w >= 5:
#             category = "Average Performer"
#         else:
#             category = "Poor Performer"
            
#         print(f"Player: {name:<12} | Tier Category: {category}")

# # 9. Generate overall collective team statistics
# def generate_team_aggregations():
#     total_runs = sum(s['runs'] for s in players.values())
#     total_wickets = sum(s['wickets'] for s in players.values())
#     total_matches = sum(s['matches'] for s in players.values())
#     return total_runs, total_wickets, total_matches

# # 10. Display top 5 batsmen
# def display_top_5_batsmen():
#     print("\n--- Top 5 Lead Batsmen Leaderboard ---")
#     sorted_batsmen = sorted(players.items(), key=lambda item: item[1]['runs'], reverse=True)
#     for i in range(5):
#         name, stats = sorted_batsmen[i]
#         print(f" {i+1}. {name:<12} - {stats['runs']} runs")

# # 11. Display top 5 bowlers
# def display_top_5_bowlers():
#     print("\n--- Top 5 Lead Bowlers Leaderboard ---")
#     sorted_bowlers = sorted(players.items(), key=lambda item: item[1]['wickets'], reverse=True)
#     for i in range(5):
#         name, stats = sorted_bowlers[i]
#         print(f" {i+1}. {name:<12} - {stats['wickets']} wickets")

# # 12. Create separate dictionary for award winners
# def get_award_winners_registry():
#     awards = {}
    
#     # Grab calculations
#     top_run_name, top_runs = get_orange_cap()
#     top_wkt_name, top_wkts = get_purple_cap()
    
#     # Map explicit award structural keys
#     awards["Orange Cap (Most Runs)"] = {"player": top_run_name, "stat": top_runs}
#     awards["Purple Cap (Most Wickets)"] = {"player": top_wkt_name, "stat": top_wkts}
    
#     # Custom rule for Tournament MVP (All round impact)
#     for name, stats in players.items():
#         if stats['runs'] > 300 and stats['wickets'] > 10:
#             awards["Tournament MVP All-Rounder"] = {"player": name, "stat": f"{stats['runs']} runs & {stats['wickets']} wkts"}
            
#     return awards


# # =====================================================================
# # Challenge: Complete Tournament Summary Report
# # =====================================================================
# def print_complete_tournament_report():
#     print("\n" + "="*55)
#     print("             OFFICIAL TOURNAMENT ANALYTICS REPORT         ")
#     print("="*55)
    
#     # Collective metrics
#     t_runs, t_wkts, _ = generate_team_aggregations()
#     avg_runs = calculate_class_run_average()
    
#     print(f"📊 Total Runs Scored Across Board : {t_runs}")
#     print(f"🎯 Total Wickets Captured          : {t_wkts} wickets")
#     print(f"📈 General Individual Run Average  : {avg_runs:.2f} runs")
#     print("-" * 55)
    
#     # Individual Honours
#     print("🏆 PRESENTATION CEREMONY HONOUR ROLL:")
#     awards_dict = get_award_winners_registry()
#     for title, data in awards_dict.items():
#         print(f" - {title:<30}: {data['player']} ({data['stat']})")
#     print("="*55)


# # =====================================================================
# # Run-Time Execution / Project Control Module
# # =====================================================================

# # Display the master sheet log grid
# display_all_players()

# # Run mathematical query filters
# display_all_rounders()
# display_above_average_batsmen()

# # Execute tier segment list transformations
# show_player_performance_categories()

# # Print leaderboards
# display_top_5_batsmen()
# display_top_5_bowlers()

# # Final challenge metric compilation output execution
# print_complete_tournament_report()


# =====================================================================
# 4. Cricket Tournament Analytics System (Menu-Driven)
# =====================================================================

players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 510, "matches": 12, "wickets": 1},
    "Rahul": {"runs": 380, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 340, "matches": 12, "wickets": 14},
    "Jadeja": {"runs": 210, "matches": 12, "wickets": 18},
    "Bumrah": {"runs": 25, "matches": 10, "wickets": 24},
    "Shami": {"runs": 12, "matches": 9, "wickets": 21},
    "Siraj": {"runs": 8, "matches": 11, "wickets": 12},
    "Kuldeep": {"runs": 35, "matches": 10, "wickets": 15},
    "Gill": {"runs": 480, "matches": 12, "wickets": 0},
    "Iyer": {"runs": 410, "matches": 12, "wickets": 0},
    "Pant": {"runs": 365, "matches": 10, "wickets": 0},
    "Sky": {"runs": 290, "matches": 12, "wickets": 1},
    "Axar": {"runs": 185, "matches": 9, "wickets": 11},
    "Ashwin": {"runs": 120, "matches": 6, "wickets": 8},
    "Thakur": {"runs": 95, "matches": 7, "wickets": 6},
    "Chahal": {"runs": 5, "matches": 5, "wickets": 7},
    "Sundar": {"runs": 110, "matches": 8, "wickets": 5},
    "Dube": {"runs": 160, "matches": 8, "wickets": 3},
    "Jaiswal": {"runs": 525, "matches": 12, "wickets": 0},
    "Rinku": {"runs": 240, "matches": 10, "wickets": 0},
    "Kishan": {"runs": 210, "matches": 6, "wickets": 0},
    "Ruturaj": {"runs": 315, "matches": 8, "wickets": 0},
    "Samson": {"runs": 190, "matches": 7, "wickets": 0},
    "Arshdeep": {"runs": 18, "matches": 12, "wickets": 17},
    "Mukesh": {"runs": 10, "matches": 6, "wickets": 5},
    "Avesh": {"runs": 4, "matches": 4, "wickets": 4},
    "Bishnoi": {"runs": 2, "matches": 5, "wickets": 6},
    "Harshit": {"runs": 15, "matches": 3, "wickets": 4},
    "Nitish": {"runs": 145, "matches": 5, "wickets": 4}
}

while True:
    print("\n=========================================")
    print("      CRICKET TOURNAMENT METRICS CORE     ")
    print("=========================================")
    print("1. Display All Player Stats")
    print("2. Find Highest Run Scorer (Orange Cap)")
    print("3. Find Lowest Run Scorer")
    print("4. Calculate Average Tournament Runs")
    print("5. Find Maximum Wickets Winner (Purple Cap)")
    print("6. Show All-Rounders Profile Pool")
    print("7. Display Batsmen Performance Above Average")
    print("8. Run Category Tier Segment Transformations")
    print("9. Show Collective Aggregate Statistics")
    print("10. Display Top 5 Batsmen Leaderboard")
    print("11. Display Top 5 Bowlers Leaderboard")
    print("12. Generate Award Winners Dictionary")
    print("13. Output Tournament Report")
    print("14. Exit Dashboard")
    print("=========================================")
    
    choice = input("Enter your choice (1-14): ")
    
    if choice == "1":
        print(f"\n{ 'Player Name':<15 }{ 'Matches':<10 }{ 'Runs':<10 }{ 'Wickets':<10 }")
        print("-" * 45)
        for name, s in players.items():
            print(f"{ name:<15 }{ s['matches']:<10 }{ s['runs']:<10 }{ s['wickets']:<10 }")
            
    elif choice == "2":
        leader = None
        for name, s in players.items():
            if leader is None or s['runs'] > players[leader]['runs']:
                leader = name
        print(f"\n🔥 Orange Cap Lead: {leader} - {players[leader]['runs']} runs scored.")
        
    elif choice == "3":
        tail = None
        for name, s in players.items():
            if tail is None or s['runs'] < players[tail]['runs']:
                tail = name
        print(f"\n📉 Lowest Run Marker: {tail} - {players[tail]['runs']} runs scored.")
        
    elif choice == "4":
        total_runs = 0
        count = 0
        for s in players.values():
            total_runs += s['runs']
            count += 1
        print(f"\n📈 Run Average Per Player: {total_runs/count:.2f} runs")
        
    elif choice == "5":
        bowler = None
        for name, s in players.items():
            if bowler is None or s['wickets'] > players[bowler]['wickets']:
                bowler = name
        print(f"\n🔮 Purple Cap Lead: {bowler} - {players[bowler]['wickets']} wickets taken.")
        
    elif choice == "6":
        print("\n--- Confirmed All-Rounder Criteria Matches (Runs > 300 & Wkts > 5) ---")
        for name, s in players.items():
            if s['runs'] > 300 and s['wickets'] > 5:
                print(f" 🏏 {name} -> Runs: {s['runs']} | Wickets: {s['wickets']}")
                
    elif choice == "7":
        total_runs = 0
        count = 0
        for s in players.values():
            total_runs += s['runs']
            count += 1
        avg = total_runs / count
        
        print(f"\n--- Outperforming Run Average ({avg:.1f} runs) ---")
        for name, s in players.items():
            if s['runs'] > avg:
                print(f" 📈 {name:<12} | {s['runs']} runs")
                
    elif choice == "8":
        print("\n--- Player Tier Segment Classifications ---")
        for name, s in players.items():
            r = s['runs']
            w = s['wickets']
            if r >= 500 or w >= 20: tier = "Star Performer"
            elif r >= 300 or w >= 12: tier = "Good Performer"
            elif r >= 100 or w >= 5: tier = "Average Performer"
            else: tier = "Poor Performer"
            print(f" Player: {name:<12} | Tier Classification: {tier}")
            
    elif choice == "9":
        runs = 0
        wkts = 0
        mtch = 0
        for s in players.values():
            runs += s['runs']
            wkts += s['wickets']
            mtch += s['matches']
        print(f"\n📊 System Collective Matrix Values -> Total Runs: {runs} | Total Wickets: {wkts} | Team Matches: {mtch}")
        
    elif choice == "10":
        batsmen_array = []
        for name, s in players.items():
            batsmen_array.append([name, s['runs']])
            
        n = len(batsmen_array)
        for i in range(n):
            for j in range(0, n-i-1):
                if batsmen_array[j][1] < batsmen_array[j+1][1]:
                    batsmen_array[j], batsmen_array[j+1] = batsmen_array[j+1], batsmen_array[j]
                    
        print("\n🏆 --- Top 5 Tournament Batting Elite ---")
        for i in range(5):
            print(f" #{i+1} {batsmen_array[i][0]:<12} | Runs: {batsmen_array[i][1]}")
            
    elif choice == "11":
        bowlers_array = []
        for name, s in players.items():
            bowlers_array.append([name, s['wickets']])
            
        n = len(bowlers_array)
        for i in range(n):
            for j in range(0, n-i-1):
                if bowlers_array[j][1] < bowlers_array[j+1][1]:
                    bowlers_array[j], bowlers_array[j+1] = bowlers_array[j+1], bowlers_array[j]
                    
        print("\n🔮 --- Top 5 Tournament Bowling Elite ---")
        for i in range(5):
            print(f" #{i+1} {bowlers_array[i][0]:<12} | Wickets: {bowlers_array[i][1]}")
            
    elif choice == "12":
        award_winners = {}
        top_bat = None
        top_bowl = None
        for name, s in players.items():
            if top_bat is None or s['runs'] > players[top_bat]['runs']: top_bat = name
            if top_bowl is None or s['wickets'] > players[top_bowl]['wickets']: top_bowl = name
        award_winners["Orange_Cap"] = {"name": top_bat, "score": players[top_bat]['runs']}
        award_winners["Purple_Cap"] = {"name": top_bowl, "score": players[top_bowl]['wickets']}
        print("\n[System] Live Presentation Map Staged:")
        print(award_winners)
        
    elif choice == "13":
        top_bat = None
        for name, s in players.items():
            if top_bat is None or s['runs'] > players[top_bat]['runs']: top_bat = name
        print("\n" + "="*50)
        print("          OFFICIAL LEAGUE SUMMARY REPORT          ")
        print("="*50)
        print(f" Tournament Leading Run Scorer: {top_bat} ({players[top_bat]['runs']} runs)")
        print("="*50)
        
    elif choice == "14":
        break