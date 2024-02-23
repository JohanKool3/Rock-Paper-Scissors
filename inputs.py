def getUserInput(min, max):

    validInput = None
    attempts = 0
    while not validInput or attempts < 3:
        
        try:
            testInput = int(input("Please enter an option: "))

            if testInput <= max and testInput >= min:
                return testInput
            
            else:
                attempts += 1
        except:
            print(f"Invalid Input, must be a number between {min} and {max}")
            attempts += 1

    return -1
        