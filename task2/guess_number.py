import random

# Generate random number
number = random.randint(1, 100)

attempts = 0

print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess >number:
        print("Too High! Try again.\n")
    elif guess <number:
        print("Too Low! Try again.\n")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
