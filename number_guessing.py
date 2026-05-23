import random
print("========number guessing game=======")

play_again = 'yes'
while play_again.lower() =='yes':
    # generate the a random number from 1 - 99 and also set the max attempt to 5 
    secret_number = random.randint(1,100)
    max_attempt = 5
    attempt = 0

    print('i have selected a number between 1 and 100')
    print(f"you have {max_attempt} left")

    # checks if the user still have attempts left 
    while attempt < max_attempt:
        try:
            # takes user input 
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100: 
                print("please enter a number between 1 and 100.\n")
                continue

            attempt += 1

            # checks if the user guess is too high, low or correct
            if guess > secret_number:
                print("too high")
            elif guess < secret_number:
                print("too low")
            else:
                print("you are correct")
                break
            print(f"attempts left: { max_attempt - attempt}\n")

        except ValueError:
            print("invalid input please enter numbers only ")
    else:
        print(f"game over! the correct number was {secret_number}")
    play_again = input("\n do u want to play again (yes/no): ")

print("\n thanks for playing")