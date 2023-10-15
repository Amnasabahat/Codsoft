import random

# Initialize scores
you_score = 0
computer_score = 0

# Game loop
while True:
    # Prompt you to choose rock, paper, or scissors
    you_choice = input("Choose rock, paper, or scissors: ").lower()

    # Generate a random choice for the computer
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner based on the choices
    if you_choice in choices:
        print(f"You chose {you_choice}. The computer chose {computer_choice}.")

        if you_choice == computer_choice:
            print("It's a tie!")
        elif (you_choice == "rock" and computer_choice == "scissors") or \
             (you_choice == "scissors" and computer_choice == "paper") or \
             (you_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            you_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print(f"You: {you_score}  Computer: {computer_score}")

        # Ask if you want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

print("Thanks for playing!")
