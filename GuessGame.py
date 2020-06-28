# Guess Game
import random
# from Live import input_validator


def generate_number(difficulty_level):

    secret_number = random.randint(1, int(difficulty_level))
    return secret_number


def get_guess_from_user(difficulty_level):
    # flag = False
    # while flag is False:
    # max_value = int(difficulty_level)
    user_guss = input("Please guess a number between 1 to " + str(difficulty_level) + ": ")
    # flag = input_validator(user_guss, int(difficulty_level))
    return user_guss


def compare_results(secret_num, user_guess_num):
    return print(int(secret_num) == int(user_guess_num), "Computer Guess: " + str(secret_num) + ", Your guess: " + str(user_guess_num))


def play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))


