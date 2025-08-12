import json

from . import utils

class Ingredient:
    def __init__(self, name : str, verbose = True):
        self.name = name

        try:
            self.load(verbose)
        except FileNotFoundError:
            self.new_info()
            self.save()


    def new_info(self):
        print("\nPlease fill in the nutritional information per 100g of " + self.name.replace("_", " "))
        self.nutrition = {}
        self.nutrition["energy"]  = float(input("Energy (kcal): "))
        self.nutrition["fat"]     = float(input("Fat (g): "))
        self.nutrition["sat_fat"] = float(input("Saturated fat (g): "))
        self.nutrition["carbs"]   = float(input("Carbohydrates (g): "))
        self.nutrition["sugar"]   = float(input("Sugar (g): "))
        self.nutrition["fiber"]   = float(input("Fiber (g): "))
        self.nutrition["protein"] = float(input("Protein (g): "))
        #self.nutrition["weight"]  = float(input("Typical weight (g): "))

        print("\nFinal table for ingredient " + self.name.replace("_", " "))
        utils.print_table(self.nutrition)

        while True:
            answer = input("Is the table correct? (y/n): ").strip().lower()
            if answer in ["yes", "y"]:
                break
            elif answer in ["no", "n"]:
                raise RuntimeError("Non-valid table")

    def replace(self):
        old = dict(self.nutrition)
        try:
            self.new_info()
            self.save()
        except RuntimeError:
            print("Ingredient not replaced")
            self.nutrition = old

    def save(self):
        with open(utils.data_ing_dir + self.name + ".json", "w") as f:
            json.dump(self.nutrition, f)

    def show(self):
        print("\nNutrition table:")
        utils.print_table(self.nutrition)

    def load(self, verbose = True):
        with open(utils.data_ing_dir + self.name + ".json", "r") as f:
            self.nutrition = json.load(f)
        if(verbose):
            print("Importing saved ingredient...")
