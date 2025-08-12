import json

import numpy as np

from .ingredient import Ingredient
from . import utils

class Recipe:
    def __init__(self, name : str):
        self.name = name
        self.ing_names = []
        self.ingredients = []
        self.weights = []

        try:
            self.load()
        except FileNotFoundError:
            print("Creating a new recipe...\n")

    def add(self, ing_name : str, weight : float):
        try:
            self.ingredients.append(Ingredient(ing_name))
        except RuntimeError:
            print("Ingredient not added")
            return
        self.ing_names.append(ing_name)
        self.weights.append(weight)
        self.save()

    def remove(self, index : int):
        del self.ing_names[index]
        del self.ingredients[index]
        del self.weights[index]
        self.save()

    def table(self):
        fractions = np.array(self.weights)/np.sum(self.weights)
        table = {}
        for key in self.ingredients[0].nutrition.keys():
            table[key] = np.sum(fractions*[i.nutrition[key] for i in self.ingredients])
        return table

    def show(self):
        if(len(self.ing_names) == 0):
            print("\nThis recipe is empty.")
            return

        print("\nIngredients:")
        for i,name in enumerate(self.ing_names):
            print(str(i) + ". " + str(self.weights[i]) + " g of " + name.replace("_", " "))

        print("\nNutrition table (per 100g):")
        tab = self.table()
        utils.print_table(tab)

    def save(self):
        with open(utils.data_rec_dir + self.name + ".json", "w") as f:
            json.dump([self.ing_names, self.weights], f)

    def load(self):
        with open(utils.data_rec_dir + self.name + ".json", "r") as f:
            self.ing_names, self.weights = json.load(f)
        for name in self.ing_names:
            self.ingredients.append(Ingredient(name, False))
        print("Importing saved recipe...")
