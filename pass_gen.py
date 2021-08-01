from random import choice, randint, shuffle
# import random

CAPITAL_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NORMAL_LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
NUMBERS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
SYMBOLS = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]
ALL_CHARACTERS_LISTS = [
    CAPITAL_LETTERS,
    NORMAL_LETTERS,
    NUMBERS,
    SYMBOLS
]


def generate():
    """
    Generates a fully random password containing at least 8 characters having numbers, normal and capital letters and
    symbols

    :return:
    """
    capital_letters_list = [choice(CAPITAL_LETTERS) for _ in range(randint(3, 8))]
    normal_letter_list = [choice(NORMAL_LETTERS) for _ in range(randint(3, 8))]
    number_list = [choice(NUMBERS) for _ in range(randint(1, 4))]
    symbol_list = [choice(SYMBOLS) for _ in range(randint(1, 4))]
    password_list = normal_letter_list + number_list + symbol_list + capital_letters_list

    shuffle(password_list)
    password = ''.join(password_list)

    return password
