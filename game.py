import re
from words import get_category_lst
GUESSES_LIMIT = 7


def pick_category(words_dict):
    """
    Use words_dict to show the category
    and asks the user to choose one
    """
    c_lst = get_category_lst(words_dict)
    for i, c in enumerate(c_lst):
        print(f"{i+1}. {c}")

    while True:
        user_choice = input(f"Enter choice number (between 1 - {len(c_lst)})")
        valid_choice = validation_input(user_choice,'number', len(c_lst))
        if valid_choice:
            break
    return c_lst[valid_choice]

def only_en_letter(user_input):
    if bool(re.fullmatch(r"[A-Za-z]+", user_input)):
        return user_input
    else:
        print(f"Please enter a valid English letter!")
        return

def validation_input(user_input, input_type, range=None):
    """
    Return the input of user choice
    only if the input is in input type and in range
    else - return None
    """
    if input_type == 'number':
        if user_input.isdigit():
            if 0 < int(user_input) < range:
                return int(user_input)
            else:
                print(f"Please enter a number between 0 to {range}")
                return
        else:
            print("Please enter a valid number!")
            return
    elif type == 'letter':
        return only_en_letter(user_input)
    
def user_attemp():
    while True:
        guess = input("Enter a letter: ")
        valid = only_en_letter(guess)
        if valid:
            return valid

def letter_exist(word, user_guess):
    return user_guess in word

def win_lose_or_continue(word, shown_word, attemps):
    if attemps > GUESSES_LIMIT:
        if word == shown_word:
            return 'win'
        else:
            return 'lose'
    else:
        return 'continue'
    
