import numpy as np

from src.ingredient import Ingredient
from src.utils import print_table 

class Recipe:
    def __init__(self, name : str):
        self.name = name
        self.ingredients = []
        self.weights = []

    def add(self, ingredient : Ingredient, weight : float):
        self.ingredients.append(ingredient)
        self.weights.append(weight)

    def delete(self, index : int):
        del self.ingredients[index]
        del self.weights[index]

    def make_table(self):
        fractions = np.array(self.weights)/np.sum(self.weights)
        table = {}
        for key in self.ingredients.nutrition[0]:
            table[key] = np.sum(fractions*[i.info[key] for i in self.ingredients])
        print("\nNutrition table of " + self.name)
        print_table(table)
            
