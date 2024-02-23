from random import choice
from inputs import getUserInput
from graphicalElements import displayGameOver, displayOptions


def game():
    options = ["Rock", "Paper", "Scissors"]

    cpuPlayer =  choice(options)

    displayOptions(options)
    # Need to convert from option to list index, -1
    playerIndex = getUserInput(1, len(options)) - 1
    playerChoice = options[playerIndex]
    
    calculateWinner(playerChoice, cpuPlayer)

def calculateWinner(player1Option, player2Option):
    
    winningCombos = {"Rock": "Scissors",
                     "Scissors": "Paper",
                     "Paper": "Rock"}

    # Draw state, both the same
    if player1Option == player2Option:
        displayGameOver(player1Option, player2Option)

    # There has to be a winner
    else:
        
        if player2Option == winningCombos[player1Option]:
            displayGameOver(player1Option, player2Option, "Player 1")

        elif player1Option == winningCombos[player2Option]:
            displayGameOver(player1Option, player2Option, "CPU")

        print("Play again?")