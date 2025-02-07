import random

random_num = random.randint(1, 20)

print("Hello! What is your name?")
name = str(input())
print(f"Well {name}, I am thinking of a number between 1 and 20")

count = 0

while True:
    guess_number = input("Take a guess: ")
    
    if guess_number.lower() == 'q':
        print("Goodbye!")
        break
    
    if not guess_number.isdigit():
        print("Please enter a number!")
        continue

    guess_num = int(guess_number)
    count += 1

    if guess_num < random_num:
        print("Your guess is too low")
    elif guess_num > random_num:
        print("Your guess is too high")
    else:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        break
