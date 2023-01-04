import random

options = ["rock", "paper", "scissors"]
players = ["", ""]

def getUserInput():
    print("Type 'rock', 'paper' or 'scissors'")
    user_input = input("Enter: ")
    #Wrong input by user:
    while  user_input not in options:
        print("That's not an option!")
        user_input = input("Enter: ")
    return user_input

def printInputs(vsComputer):
    if vsComputer == True:
        print("Computer: ",players[1])
        print("Player: ",players[0])
    else:
        print("Player 1: ",players[0])
        print("Player 2: ",players[1])

def getWinner(playerName1, playerName2):
    if players[0] == "rock" and players[1] == "scissors" or players[0] == "scissors" and players[1] == "paper" or players[0] == "paper" and players[1] == "rock":
        print(playerName1, "won!")
    elif players[0] == players[1]:
        print("It's a draw!")
    else:
        print(playerName2, " won!")

#Player vs computer mode
def vsComputer():
    print("You vs the computer!")
    players[0] = getUserInput()
    #Get random input from computer
    players[1] = options[random.randint(0,2)]
    printInputs(True)
    getWinner("Player", "Computer")

#Player vs Player mode
def vsPlayer():
    print("Player vs Player!")
    players[0] = getUserInput()
    players[1] = getUserInput()
    printInputs(False)
    getWinner("Player 1", "Player 2")

#Wrapper function
def main():
    print("Welcome to rock paper scissors!")
    while True:
        print("Choose your mode: (1) Player vs Player (2) Player vs Computer (3) Quit")
        user_input = int(input("Input: "))
        if user_input == 1:
            vsPlayer()
        elif user_input == 2:
            vsComputer()
        elif user_input == 3:
            break
        else:
            print("Invalid input, pls try again!")
#Run programm
main()