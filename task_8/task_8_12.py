import random


def game():
    while True:
        text = input('Rock, paper or scissor? (print \'exit\' to end game) ').lower()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        if text == computer_choice:
            result = "Tie"
        elif text == "rock" and computer_choice == "Scissors" or\
                text == "paper" and computer_choice == "Rock" or\
                text == "scissors" and computer_choice == "Paper":
            result = "Player wins"
        elif text == 'exit':
            return 'Thx for playing!'
        else:
            result = "Computer wins"
        print(result)


print(game())
