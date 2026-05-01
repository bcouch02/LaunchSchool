import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_ABBREVIATIONS = ["r", "p", "s", "l", "sp"]
PLAYER_SCORE = 0
COMPUTER_SCORE = 0


def prompt(message):
    print(f"==> {message}")


def display_winner(player, computer):
    global PLAYER_SCORE, COMPUTER_SCORE
    if (
        (player == "rock" and computer == "scissors")
        or (player == "rock" and computer == "lizard")
        or (player == "paper" and computer == "rock")
        or (player == "paper" and computer == "spock")
        or (player == "scissors" and computer == "paper")
        or (player == "scissors" and computer == "lizard")
        or (player == "lizard" and computer == "spock")
        or (player == "lizard" and computer == "paper")
        or (player == "spock" and computer == "scissors")
        or (player == "spock" and computer == "rock")
    ):
        prompt("You win!")
        PLAYER_SCORE += 1
    elif (
        (player == "rock" and computer == "paper")
        or (player == "rock" and computer == "spock")
        or (player == "paper" and computer == "scissors")
        or (player == "paper" and computer == "lizard")
        or (player == "scissors" and computer == "rock")
        or (player == "scissors" and computer == "spock")
        or (player == "lizard" and computer == "rock")
        or (player == "lizard" and computer == "scissors")
        or (player == "spock" and computer == "paper")
        or (player == "spock" and computer == "lizard")
    ):
        prompt("Computer wins!")
        COMPUTER_SCORE += 1
    else:
        prompt("It's a tie!")
        
################################################################################

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES and choice not in VALID_CHOICES_ABBREVIATIONS:
        prompt("That's not a valid choice.")
        choice = input()

    if choice[0].lower() == "r":
        choice = "rock"
    elif choice[0].lower() == "p":
        choice = "paper"
    elif choice[0].lower() == "s":
        choice = "scissors"
    elif choice[0].lower() == "l":
        choice = "lizard"
    elif choice[0].lower() == "sp":
        choice = "spock"

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)
    if COMPUTER_SCORE < 3 and PLAYER_SCORE < 3:
        prompt(f"Current score - You: {PLAYER_SCORE}, Computer: {COMPUTER_SCORE}")
        
    prompt("Do you want to play again? (y/n)")
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == "n":
        break
