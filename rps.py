import random

def main():

    # STEP 1: Computer picks a random play
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)

    # STEP 2: Take player input and validate it
    player = input("Enter rock, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid input! Please type rock, paper, or scissors.")
        return

    # STEP 2 (cont.) + STEP 3: Compare and print the result
    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")

main()