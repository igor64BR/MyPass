import random

CHARACTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+'
]
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
    val_let = False
    val_cap = False
    val_num = False
    val_sym = False
    total_val = [val_let, val_cap, val_sym, val_num]

    password = ''

    for _ in range(random.randint(8, 16)):
        password += random.choice(CHARACTERS)

    for index in range(4):
        for char in ALL_CHARACTERS_LISTS[index]:
            if char in password:
                total_val[index] = True

    for val in total_val:
        if not val:
            generate()

    return password
