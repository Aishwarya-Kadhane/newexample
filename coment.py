import random

name = input("ARE YOU READYYYY: ")


def playerPlays():
    return input("Choose between rock, paper, and scissors: ").lower()


def computerPlays():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def getGameResult(player_choice, computer_choice):
    rules = {
        "rock": {
            "rock": "It's a draw",
            "paper": "You lose",
            "scissors": "You win"
        },
        "paper": {
            "rock": "You win",
            "paper": "It's a draw",
            "scissors": "You lose"
        },
        "scissors": {
            "rock": "You lose",
            "paper": "You win",
            "scissors": "It's a draw"
        }
    }

    return rules[player_choice][computer_choice]


while True:

    player_choice = playerPlays()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = computerPlays()

    print(f"Computer plays: {computer_choice}")

    game_result = getGameResult(player_choice, computer_choice)

    print(game_result)

    if "lose" in game_result:
        print(f"You lost to the computer. Thanks for playing, {name}!")
        break

