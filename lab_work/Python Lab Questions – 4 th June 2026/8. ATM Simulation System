#Problem Statement: Initial Balance = ₹10,000 Display a menu repeatedly: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit Requirements: • Withdrawal should not exceed balance. • Display appropriate messages. • Continue until Exit is selected.  

# --- Step 1: Set up the initial account balance ---
balance = 10000

# --- Step 2: Start the continuous menu loop ---
while True:
    print("\n" + "="*12 + " ATM SERVICES " + "="*12)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 38)
    
    # Take choice input from the user
    choice = input("Choose an option (1-4): ")
    
    # --- Option 1: Check Balance ---
    if choice == "1":
        print(f"\nYour current account balance is: ₹{balance}")
        
    # --- Option 2: Deposit ---
    elif choice == "2":
        deposit_amount = float(input("\nEnter the amount to deposit: ₹"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Successfully deposited ₹{deposit_amount}. New Balance: ₹{balance}")
        else:
            print("Invalid amount! Deposit must be greater than zero.")
            
    # --- Option 3: Withdraw ---
    elif choice == "3":
        withdraw_amount = float(input("\nEnter the amount to withdraw: ₹"))
        
        # Validation Check: Don't allow negative values or withdrawing more than available
        if withdraw_amount <= 0:
            print("Invalid amount! Please enter a valid sum to withdraw.")
        elif withdraw_amount > balance:
            print(f"Transaction Denied! Insufficient funds. Available Balance: ₹{balance}")
        else:
            balance -= withdraw_amount
            print(f"Successfully withdrawn ₹{withdraw_amount}. Remaining Balance: ₹{balance}")
            
    # --- Option 4: Exit ---
    elif choice == "4":
        print("\nThank you for using our ATM. Have a great day ahead!")
        break  # This breaks the loop instantly and ends the program
        
    # --- Fallback: Handle invalid menu inputs ---
    else:
        print("Invalid choice! Please select a valid option from 1 to 4.")