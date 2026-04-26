import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()
