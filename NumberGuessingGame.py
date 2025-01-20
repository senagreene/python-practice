import random


def mode(chances):
    randomNum = random.randint(1, 100)
    attempt = 0
    while attempt < chances:
        try:
            userGuess = int(input("enter a number between 1 and 100: "))
            if userGuess > 100 or userGuess < 1:
                print("Invalid input.Please enter a number between 1 and 100")
                continue  # asks for input again if it is out of range
        except ValueError:
            print("Invalid input")
            continue  # asks for input again if it is a invalid number
        attempt += 1

        if (userGuess == randomNum):
            print("Congratulations! You guessed the correct number ")
            return  # end the game if user guesses correct number
        else:
            if (randomNum > userGuess):
                print(f"Incorrect!The number is greater than {userGuess}")
            elif (randomNum < userGuess):
                print(f"Incorrect!The number is less than {userGuess}")

        if attempt == chances:
            print(
                f"You have used all your chances.The correct number was {randomNum}")


# CLI
while True:
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.\n You have 5 chances to guess the correct number.")
    print("Please select the difficulty level:"
          "\n1.Easy (10 chances)"
          "\n2. Medium (5 chances)"
          "\n3. Hard (3 chances)"
          "\n4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Great! You have selected the Easy difficulty level.Let's start the game!")
        mode(10)

    elif choice == '2':
        print("Great! You have selected the Medium difficulty level.Let's start the game!")
        mode(5)

    elif choice == '3':
        print("Great! You have selected the Hard difficulty level.Let's start the game!")
        mode(3)
    elif choice == '4':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")
