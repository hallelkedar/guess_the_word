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
    word_dict = {}
    current_category = None

    with open(file_path) as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            elif line.endswith("#"):
                    current_category = line[1:].strip()
                    word_dict[current_category] = []

            else:
                word_dict[current_category] = line
    return word_dict

def get_category_lst(word_dict):
    category_lst = []
    
    for category in word_dict:
        category_lst.append(category)
    return category_lst

def get_random_word(word_dict, category):
    word_lst = word_dict[category]
    random_index = random.randint(0, (len(word_lst)-1))
    
    return word_lst[random_index]
