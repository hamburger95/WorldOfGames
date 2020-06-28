# Live
from MemoryGame import play as play_memo
from GuessGame import play as play_guess
from CurrencyRouletteGame import play as play_cur
from input_validator import input_validator
from Utils import clear_screen
from Score import add_score

memory_game_desc = "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back."
guess_game_desc = "2. Guess Game - guess a number and see if you chose like the computer."
cur_game_desc = "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
exit_desc = "4. Exit"


def welcome(name):
    welcome_msg = "Hello " + name + " and welcome to the world of Games(WoG)."
    second_msg = "Here you can find many cool games to play."
    return "\n" + welcome_msg + "\n" + second_msg


def load_game():

    # entry no.1
    entry_no_1 = False
    while entry_no_1 is False:
        max_value = 4
        print("\n" + memory_game_desc + "\n", "\n" + guess_game_desc + "\n", "\n" + cur_game_desc + "\n" + "\n" + exit_desc + "\n")
        game_id = input("Please choose a game to play:" + "\n")
        entry_no_1 = input_validator(game_id, max_value)

    if int(game_id) == 4:
        exit()

    # entry no.2
    entry_no_2 = False
    while entry_no_2 is False:
        max_value = 5
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        entry_no_2 = input_validator(difficulty, max_value)
    # menu
    choice = ''
    choice = int(game_id)
    if choice == 1:
        play_memo(int(difficulty))
        clear_screen()
        add_score(difficulty)
        load_game()
    elif choice == 2:
        play_guess(int(difficulty))
        clear_screen()
        add_score(difficulty)
        load_game()
    elif choice == 3:
        play_cur(int(difficulty))
        clear_screen()
        add_score(difficulty)
        load_game()
    else:
        print('something went wrong...choice: ', choice, "type: ", type(choice))




