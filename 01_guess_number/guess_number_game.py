import random


def check_and_return_integer(value):
    while not value.isdigit():
        print("Provided value is not a number...")
        value = input("Enter a valid number: ")
    return int(value)


top_range = input("Enter a top range value: ")
top_range_number = check_and_return_integer(top_range)

while top_range_number < 1:
    print("Provided number is less than 1...")
    top_range = input("Please provide a top range number again...")
    top_range_number = check_and_return_integer(top_range)

# numb = random.randrange(10)
random_number = random.randint(0, top_range_number)
print(random_number)

number_of_guesses = 0

user_choice = input("Guess a number: ")
user_choice_number = check_and_return_integer(user_choice)
number_of_guesses += 1

while user_choice_number != random_number:

    if user_choice_number > random_number:
        print("You're above a number!")
    else:
        print("You're below a number!")

    user_choice = input("Try to guess again: ")
    user_choice_number = check_and_return_integer(user_choice)
    number_of_guesses += 1

print(f"Your guess was correct after {number_of_guesses} guesses!")
