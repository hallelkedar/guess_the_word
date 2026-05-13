import re
from words import get_category_lst, get_random_word
from utils.time_utils import day_or_night

MENU_ASCII = """
 $$$$$$\                                                  $$\     $$\                       $$\            $$\     $$\                         
$$  __$$\                                                 $$ |    $$ |                      $$ |           $$ |    $$ |                        
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$ | $$$$$$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$ |$$  __$$\\_$$  _|\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |$$$$$$$$ | $$ |    $$ |    $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |$$   ____| $$ |$$\ $$ |$$\ $$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |\$$$$$$$\  \$$$$  |\$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__| \_______|  \____/  \____/  \_______|\__|      
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               """
MENU = """
            1. Start Game (random category)
            2. Choose Category
            3. Exit
    """
MENU_OPTIONS_NUMBER = 3
GUESSES_LIMIT = 15
AGAIN = 'again'
EXIT = 'exit'

def pick_category():
    """
    Use words_dict to show the category
    and asks the user to choose one
    """
    c_lst = get_category_lst()
    for i, c in enumerate(c_lst):
        print(f"{i+1}. {c}")

    while True:
        user_choice = input(f"Enter choice number (between 1 - {len(c_lst)}): ")
        valid_choice = validation_input(user_choice,'number', len(c_lst))
        if valid_choice:
            return c_lst[valid_choice-1]
        
def only_en_letter(user_input):
    if bool(re.fullmatch(r"[A-Za-z]+", user_input)) and len(user_input) == 1:
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
            if 0 < int(user_input) <= range:
                return int(user_input)
            else:
                print(f"Please enter a number between 0 to {range}")
                return
        else:
            print("Please enter a valid number!")
            return
    elif input_type == 'letter':
        return only_en_letter(user_input)

def menu_printing():
    print(MENU_ASCII)
    print(MENU)

def get_the_word():
    """
    show the menu and return the hidden word
    by the user choosing category (or random)
    """
    menu_printing()
    while True:
        choice = input("Choose one: ")
        valid_choice = validation_input(choice, 'number', MENU_OPTIONS_NUMBER)
        if valid_choice == 1:
            return get_random_word()
        elif valid_choice == 2:
            return get_random_word(pick_category())
        elif valid_choice == 3:
            print(f'Have a good {day_or_night()}...')
            exit()

def user_letter_guess():
    while True:
        guess = input("Enter a letter: ")
        valid = validation_input(guess, 'letter')
        if valid:
            return valid

def user_proccess_display(hidden_word, attempts, wrong_l):
   print(f"""
┌──────────────────────────────────────┐
│ ► WORD : {' '.join(hidden_word)}
│ ♥ HP   : {attempts}
│◆ GUESSED: {' '.join(f"'{l}'" for l in wrong_l)}
└──────────────────────────────────────┘
""")

def letter_exist(word, user_guess):
    return user_guess in word

def already_guessed(letter, correct_letters, wrong_letters):
    return letter in (correct_letters + wrong_letters)

def correct_guess(word, letter, correct_letters, hidden_word_lst):
    
    print("Correct!")

    correct_l_indexes = [i for i, char in enumerate(word) if char == letter]
    for i in correct_l_indexes:
        hidden_word_lst[i] = letter
    correct_letters.append(letter)

def wrong_guess(letter, wrong_letters):
    print("Wrong letter...")
    wrong_letters.append(letter)

def guess_turn(word, letter, correct_letters, wrong_letters, hidden_word_lst):
    
    if already_guessed(letter, correct_letters, wrong_letters):
        print("Youv'e already try this letter.")
        return False
    if letter_exist(word, letter):
        correct_guess(word, letter, correct_letters, hidden_word_lst)
        return False
    else:
        wrong_guess(letter, wrong_letters)
        return True

def win_and_lose_or_continue(word, shown_word, attempts, limit):

    if word == ''.join(shown_word):
        print_game_over(word, 'CONGRATULATIONS ✓ !')
        choice = game_over_options()
        return 'win', choice
    
    if attempts > limit:  
        print_game_over(word, 'GAME OVER ✖ !')
        choice = game_over_options()
        return 'lose', choice
        
    return 'continue', None
    
def print_game_over(word, msg):
    print(f"""
=========================
      {msg}
=========================
""")
    print(f"The word was: {word}")
    print("""
          Thanks for playing !

          1. Play again
          2. Exit the game
          """)

def game_over_options():

    while True:
        user_choice = input('Enter your choice: ')
        if validation_input(user_choice, 'number', 2):
            if user_choice == '1':
                return AGAIN
            return EXIT

def game_loop():

    user_attempts = 0
    wrong_letters = []
    correct_letters = []

    word = get_the_word()
    hidden_word_lst = ['_' for _ in word]

    while True:
        user_proccess_display(
        hidden_word_lst,
        (GUESSES_LIMIT - user_attempts),
        wrong_letters
        )

        letter = user_letter_guess()

        is_wrong = guess_turn(
            word,
            letter,
            correct_letters, 
            wrong_letters, 
            hidden_word_lst
            )
            
        if is_wrong:
            user_attempts += 1

        status, choice = win_and_lose_or_continue(
            word, 
            hidden_word_lst, 
            user_attempts, 
            GUESSES_LIMIT
        )
                
        if status != 'continue':
            return choice
            
