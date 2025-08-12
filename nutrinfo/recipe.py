import numpy as np

from .ingredient import Ingredient
from .utils import print_table 

class Recipe:
    def __init__(self, name : str):
        self.name = name
        self.ing_names = []
        self.ingredients = []
        self.weights = []

    def add(self, ing_name : str, weight : float):
        self.ing_names.append(ing_name)
        self.ingredients.append(Ingredient(ing_name))
        self.weights.append(weight)

    def delete(self, index : int):
        del self.ing_names[index]
        del self.ingredients[index]
        del self.weights[index]

    def make_table(self):
        fractions = np.array(self.weights)/np.sum(self.weights)
        table = {}
        for key in self.ingredients[0].nutrition.keys:
            table[key] = np.sum(fractions*[i.nutrition[key] for i in self.ingredients])
        print("\nNutrition table of " + self.name)
        print_table(table)

    def save(self):
        with open(utils.data_rec_dir + self.name + ".json", "w") as f:
            json.dump(self, f)

def load_recipe(name):
    with open(utils.data_rec_dir + name + ".json", "r") as f:
        recipe = json.load(f)
    print("Found recipe for " + self.name)
    recipe.make_table()
    return recipe
