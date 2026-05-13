from pathlib import Path
import random

DATA_DIR = "data"
FILE_NAME = "words_lst.txt"

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

            if line.startswith("#"):
                current_category = line[1:].strip()
                words_dict[current_category] = []

            else:
                if current_category is not None:
                    words_dict[current_category].append(line)
    return words_dict

def get_category_lst():
    category_lst = []
    
    for category in get_word_dict(file_path):
        category_lst.append(category)
    return category_lst

def get_random_category():
    category_lst = get_category_lst()
    return random.choice(category_lst)

def get_random_word(category=None):
    words_dict = get_word_dict(file_path)
    if category:
        word_lst = words_dict[category]
    else:
        word_lst = words_dict[get_random_category()]
    return random.choice(word_lst)