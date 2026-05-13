from words import get_random_word
from game import get_the_word

GUESSES_LIMIT = 7

MENU = """
======= Welcome to Guess The Word ! ======
            1. Start Game (random category)
            2. Choose Category
            3. Exit
    """

user_attemps = 0
word_disable = True
wrong_letter = []


def main():
    word = get_the_word(MENU, GUESSES_LIMIT)

if __name__ == '__main__':
    main()