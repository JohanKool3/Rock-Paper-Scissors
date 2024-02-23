from graphicalElements import displayMenu, displayCredits
from inputs import getUserInput
from rockPaperScissors import game

def main():
    running = True
    MIN = 1
    MAX = 3

    while running:
        displayMenu()
        option = getUserInput(MIN, MAX)

        if option == 1:
            game()

        elif option == 2:
            displayCredits()

        elif option == 3:
            quit()

        else:
            print(f"Please enter a number between {MIN} and {MAX}")

if __name__ == "__main__":
    main()