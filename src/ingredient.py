import json
import src.utils as utils

class Ingredient:
    def __init__(self, name : str):
        self.name = name

        try:
            self.load()
        except FileNotFoundError:
            self.new_info()


    def new_info(self):
        print("\nPlease fill in the nutritional information per 100g of " + name)
        self.nutrition = {}
        self.nutrition["energy"]  = float(input("Energy (kcal):"))
        self.nutrition["fat"]     = float(input("Fat (g):"))
        self.nutrition["sat_fat"] = float(input("Saturated fat (g)"))
        self.nutrition["carbs"]   = float(input("Carbohydrates (g):"))
        self.nutrition["sugar"]   = float(input("Sugar (g):"))
        self.nutrition["fiber"]   = float(input("Fiber (g):"))
        self.nutrition["protein"] = float(input("Protein (g):"))
        self.nutrition["weight"]  = float(input("Typical weight (g):"))

        print("\nFinal table:")
        utils.print_table(self.nutrition)

        while True:
            answer = input("Is the table correct? (y/n): ").strip().lower()
            if answer in ["yes", "y"]:
                break
            elif answer in ["no", "n"]:
                raise RuntimeError("Non-valid table")

    def save(self):
        with open(utils.data_dir + self.name + ".json", "w") as f:
            json.dump(self.nutrition, f)

    def load(self):
        with open(utils.data_dir + self.name + ".json", "r") as f:
            self.nutrition = json.load(f)
        print("Found nutrition table for " + self.name)
        utils.print_table(self.nutrition)
