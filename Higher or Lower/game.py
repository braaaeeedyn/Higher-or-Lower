from art import logo
from gamedata import data
import random



def playGame():
    score = 0
    correct = True
    while correct:
        accountA = random.choice(data)
        accountB = random.choice(data)
        if accountA == accountB:
            accountA = random.choice(data)
        print(logo)
        print("Who has more Followers?")
        print("Current Score "+ str(score) + "\n")
        print(accountA['name'] + "\nOr")
        print(accountB['name'] +"\n")
        choice = input("Choose your person by Typing their whole name: ")
        if choice == accountA['name']:
            if accountA['follower_count'] > accountB['follower_count']:
                score += 1
            else:
                correct = False
        elif choice == accountB['name']:
            if accountB['follower_count'] > accountA['follower_count']:
                score += 1
            else:
                correct = False
    return score

print("You got " + str(playGame()) + " Points!")

playAgain = True
while playAgain:
    playMore = input("Do you want to play again? 'y' or 'n'")
    if playMore == "y":
        print("You got " + str(playGame()) + " Points!")
    else:
        playAgain = False