def displayMenu():

    print("""
          1. Play
          2. Credits
          3. Quit
          """)
    

def displayCredits():
    print("="*20)
    print("""
        AUTHOR: Johannes Kool
        DATE: 23/02/2024
          """)
    print("="*20)

def displayOptions(options):

    index = 1

    for item in options:
        print(f"{index}. {item} \n")
        index += 1

    print("\n")
        

def displayGameOver(player1Opt, player2Opt, winner=None):

    if winner:
        print("="*20)
        print(f"Player : {winner} wins! P1: {player1Opt} | CPU: {player2Opt}")
        print("="*20)

    else:
        print("="*20)
        print(f"No one wins, it is a draw! P1: {player1Opt} | CPU: {player2Opt}")
        print("="*20)