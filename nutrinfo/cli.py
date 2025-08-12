import cmd
from pathlib import Path

from . import utils
from .recipe import Recipe
from .ingredient import Ingredient

class REPL(cmd.Cmd):
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.active_recipe = False
        self.active_ingredient = False

    def help_recipe(self):
        print("\n\trecipe [name]\n\nCreate a new recipe or load an existing one (in case a file with the same name already exists).\nSpaces and underscores are not distinguishable in the name.\n")

    def do_recipe(self, arg):
        if(utils.is_valid_filename(arg)):
            name = arg.replace(" ", "_")
            self.recipe = Recipe(name)
            self.prompt = "(" + name + ") >>> "
            self.active_recipe = True
            self.active_ingredient = False

    def help_add(self):
        print("\n\tadd [name]\n\nAdd an ingredient to the active recipe.\nSpaces and underscores are not distinguishable in the name.\n") 

    def do_add(self, arg):
        if(not self.active_recipe):
            print("Please activate a recipe first")
            return
        if(utils.is_valid_filename(arg)):
            name = arg.replace(" ", "_")
            print("Adding " + name + " to the ingredients...")
            weight = float(input("Input the weight (g): "))
            self.recipe.add(name, weight)

    def help_remove(self):
        print("\n\tremove index\n\nRemove the ingredient with the chosen index from  the active recipe\n")

    def do_remove(self, arg):
        if(not self.active_recipe):
            print("Please activate a recipe first")
            return
        self.recipe.remove(int(arg))

    def help_ingredient(self):
        print("\n\tingredient [name]\n\nCreate a new ingredient or load an existing one (in case a file with the same name already exists).\nSpaces and underscores are not distinguishable in the name.\n")

    def do_ingredient(self, arg):
        if(utils.is_valid_filename(arg)):
            name = arg.replace(" ", "_")
            self.ingredient = Ingredient(name)
            self.prompt = "[" + name + "] >>> "
            self.active_recipe = False
            self.active_ingredient = True

    def do_replace(self, arg):
        """Replace the nutrition table of the active ingredient"""
        if(not self.active_ingredient):
            print("Please activate an ingredient first")
            return
        self.ingredient.replace()

    def do_show(self, arg):
        """Show the nutritional information of the active recipe or ingredient"""
        if(self.active_recipe):
            self.recipe.show()
        elif(self.active_ingredient):
            self.ingredient.show()
        else:
            print("Please activate a recipe or ingredient first")

    def do_list(self, arg):
        """List all locally saved recipes and ingredients""" 
        recipes = [f.stem for f in Path(utils.data_rec_dir).glob("*.json")]
        if(len(recipes) == 0):
            print("\nNo recipes found!")
        else:
            print("\nSaved recipes:")
            for recipe in recipes:
                print("\t- " + recipe.replace("_", " "))

        ingredients = [f.stem for f in Path(utils.data_ing_dir).glob("*.json")]
        if(len(ingredients) == 0):
            print("\nNo ingredients found!")
        else:
            print("\nSaved ingredients:")
            for ingredient in ingredients:
                print("\t- " + ingredient.replace("_", " "))
        print()

    def do_EOF(self, arg):
        """Exit the current recipe. If there is no active recipe, exit the REPL. Call with Ctrl-D"""
        if(self.active_recipe):
            self.active_recipe = False
            print("\nExiting recipe...")
            self.prompt = ">>> " 
        elif(self.active_ingredient):
            self.active_ingredient = False
            print("\nExiting ingredient...")
            self.prompt = ">>> " 
        else:
            print("\nExiting...")
            return True

    def emptyline(self):
        pass # Do nothing on empty input

def main():
    REPL().cmdloop("Welcome to nutrinfo! Type 'help' for documentation. Exit with Ctrl-D")

if __name__ == '__main__':
    main()

