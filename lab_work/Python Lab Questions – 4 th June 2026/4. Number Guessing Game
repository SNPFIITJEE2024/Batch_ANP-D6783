#Problem Statement: Generate a secret number between 1 and 50. Allow the user to keep guessing until the correct number is found.Display: • "Too High" • "Too Low" • "Correct Guess" Also display the total number of attempts.

# Set the secret target number between 1 and 50
secret_number = 27

# Initialize the attempt tracking counter
attempts = 0

print("--- Welcome to the Number Guessing Game (1 to 50) ---")

# Start an infinite loop that breaks only when the correct guess is made
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increment the counter for every attempt made
    
    # Check the user's guess against the secret number
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess!")
        break  # Exit the loop immediately since the user won

# Display the final score/performance summary
print(f"Total number of attempts: {attempts}")