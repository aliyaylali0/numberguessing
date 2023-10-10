import random
print("""
███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████  ██    ██ ███████ ███████ ███████ ██ ███    ██  ██████  
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██    ██ ██      ██      ██      ██ ████   ██ ██       
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ██    ██ █████   ███████ ███████ ██ ██ ██  ██ ██   ███ 
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██    ██ ██           ██      ██ ██ ██  ██ ██ ██    ██ 
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████   ██████  ███████ ███████ ███████ ██ ██   ████  ██████  
                                                                                                                          
                                                                                                                          
""")

numbers = []
easy_attempts = 10
hard_attempts = 5

def keep_count():
    for number in range(1,101):
        numbers.append(number)
    global guessing_number
    guessing_number = random.choice(numbers)
    return guessing_number

def gues_number():
    your_guess = input("Make a guess: ")
    if int(your_guess) == int(guessing_number):
        print("*****Congratulations*****")
    if int(your_guess) < int(guessing_number):
        print("Too high")
    if int(your_guess) > int(guessing_number):
        print("Too low.")




print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    game = True
    keep_count()
    while game:
        print(f"You have {easy_attempts} attempts remaining to guess the number")

        gues_number()
        easy_attempts -= 1
        if easy_attempts == 0:
            print("YOU LOSE")
            print(guessing_number)
            game = False

elif difficulty == "hard":
    game = True
    keep_count()
    while game:
        print(f"You have {hard_attempts} attempts remaining to guess the number")

        gues_number()
        hard_attempts -= 1
        if hard_attempts == 0:
            print("YOU LOSE")
            print(guessing_number)
            game = False

else:
    print("Please make sure you entered correctly.")


