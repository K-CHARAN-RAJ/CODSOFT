import random
options = ("rock", "paper", "scissors")

player_score = 0
computer_score = 0

running = True

name = input("enter your name:")

while running:

    player = None
    computer = random.choice(options)



    while player not in options:
        player = input(f"Hey! {name} ready!? rock, paper, scissors.....shoot!!: ").strip().lower()

        if player not in options:
            print("huh!? thats against the rules lets go again..!!")
            continue

    print(f"{name} choose: {player}")
    print(f"computer choose: {computer}")

    if player == computer:
        print("its a tie!!!")
    elif player =="rock" and computer == "scissors":
        print("you win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("you win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("you win!")
        player_score += 1
    else:
        print("you lose.. :(")
        computer_score += 1

    print(f"Scores - You: {player_score}, Computer: {computer_score}")
    if not input ("u wanna play again? ;D (y/n):").strip().lower() == "y":
        running = False
print("game over.. @_@")