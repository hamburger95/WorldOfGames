import currency_converter
import random


r = random.randint(1, 100)
c = currency_converter.CurrencyConverter()
t = int(c.convert(r, 'USD', 'ILS'))


def get_money_interval(user_guess, d):
    max_value = t + (5 - d)
    min_value = t - (5 - d)
    return print(max_value > user_guess > min_value, "Convert Calculation is: ", t, "\nAnswer Range is between ", min_value, " and ", max_value, "Your Guess is: ", user_guess)


def get_guess_from_user():
    guess = input("Guess the value of: " + str(r) + " USD in ILS: ")
    return int(guess)


def play(difficulty):
    d = int(difficulty)
    return get_money_interval(get_guess_from_user(), d)





