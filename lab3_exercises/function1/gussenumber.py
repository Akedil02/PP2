import random

user_name = input("Hello! What is your name?\n")

print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
secret_number = random.randint(1, 20)
guessed_number = 0
guess_count = 0

while guessed_number != secret_number:
    guessed_number = int(input("Take a guess.\n"))
    guess_count += 1
    
    if guessed_number < secret_number:
        print("Your guess is too low.")
    elif guessed_number > secret_number:
        print("Your guess is too high.")

print(f"Good job, {user_name}! You guessed my number in {guess_count} guesses!")
