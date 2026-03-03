import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    if (player, computer) in wins:
        return "player"
    return "computer"

print("Rock, Paper, Scissors!")
while True:
    player = input("\nEnter rock, paper, or scissors (or 'quit'): ").lower()
    if player == "quit":
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    result = get_winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")
