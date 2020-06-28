from os import system, name
from time import sleep

SCORES_FILE_NAME = "Scores.txt"  # A string representing a file name. By default “Scores.txt”

# BAD_RETURN_CODE = 0  # - A number representing a bad return code for a function


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear_screen()



