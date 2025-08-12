import sys
import os

from tabulate import tabulate

def check_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

data_dir = os.getcwd() + "/nutrinfo/"
check_dir(data_dir)
data_ing_dir = data_dir + "/ingredients/"
check_dir(data_ing_dir)
data_rec_dir = data_dir + "/recipes/"
check_dir(data_rec_dir)

def print_table(nutrition):
    pretty_dict = {}
    pretty_dict["Energy"] = str(nutrition["energy"]) + " (kcal)"
    pretty_dict["Fat"] = str(nutrition["fat"]) + " (g)"
    pretty_dict[" -Saturated"] = str(nutrition["sat_fat"]) + " (g)"
    pretty_dict["Carbohydrates"] = str(nutrition["carbs"]) + " (g)"
    pretty_dict[" -Sugar"] = str(nutrition["sugar"]) + " (g)"
    pretty_dict[" -Fiber"] = str(nutrition["fiber"]) + " (g)"
    pretty_dict["Protein"] = str(nutrition["protein"]) + " (g)"
    print(tabulate(nutrition.items(), headers=[], tablefmt="grid"))

import re
import sys

def is_valid_filename(filename: str) -> bool:
    # Common invalid characters on Windows and Unix
    invalid_chars = r'<>:"/\\|?*\0.'
    if any(char in filename for char in invalid_chars):
        print("Error: name has an invalid character " + char)
        return False

    # No empty or just whitespace
    if filename.strip() == '':
        print("Error: name is empty")
        return False

    return True
