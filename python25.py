import random

secret_number = random.randint(1, 20)
attempts_left = 5

print("Guess the number between 1 and 20. You have 5 attempts.")

while attempts_left > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    attempts_left -= 1
    print("Attempts left:", attempts_left)

if attempts_left == 0:
    print("Out of attempts. The number was", secret_number)
