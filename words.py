from pathlib import Path
import random

DATA_DIR = "data"
FILE_NAME = "word_lst.txt"

file_path = Path(__file__).parent / DATA_DIR / FILE_NAME

def get_word_dict(file_path: Path) -> dict:
    """
    Gets file path
    and return dictionary of categories and their word list
    """
    words_dict = {}
    current_category = None

    with open(file_path) as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            elif line.endswith("#"):
                    current_category = line[1:].strip()
                    words_dict[current_category] = []

            else:
                words_dict[current_category] = line
    return words_dict

def get_category_lst(words_dict):
    category_lst = []
    
    for category in words_dict:
        category_lst.append(category)
    return category_lst

def get_random_word(category):
    
    words_dict = get_word_dict(file_path)
    word_lst = words_dict[category]
    return random.choice(word_lst)