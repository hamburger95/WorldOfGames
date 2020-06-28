import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def generate_sequence(difficulty_l):
    random_numbers_list = []
    while len(random_numbers_list) < difficulty_l:
        random_numbers_list.append(random.randint(1, 101))
    return random_numbers_list


def get_list_from_user(difficulty_len):
    user_list = []
    counter = int(difficulty_len)
    while len(user_list) < difficulty_len:
        user_list.append(int(input("Please enter your guess number...you have " + str(counter) + " number/s to enter.")))
        counter -= 1
    return user_list


def is_equal(list_a, list_b):
    return print(list_a == list_b, "Computer Guess: ", list_a, "Your Guess: ", list_b)


def play(difficulty):
    sequence_list = generate_sequence(int(difficulty))
    display_rand_list_to_user(sequence_list)
    user_list = get_list_from_user(int(difficulty))
    return is_equal(sequence_list, user_list)


def display_rand_list_to_user(rand_list):
    img = Image.new('RGB', (300, 200), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((100, 100), str(rand_list), fill=(28, 167, 57))
    image_itself = img
    image_numpy_format = np.asarray(image_itself)
    plt.imshow(image_numpy_format)
    plt.draw()
    plt.pause(2)  # pause how many seconds
    plt.close()
