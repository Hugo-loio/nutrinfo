import sys
import os

from tabulate import tabulate

def check_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

data_dir = sys.path[0] + "/nutrinfo/"
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
