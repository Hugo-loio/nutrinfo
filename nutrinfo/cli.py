import cmd
from pathlib import Path

from . import utils
from .recipe import Recipe
from .ingredient import Ingredient

class REPL(cmd.Cmd):
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.recipe = None
    
    def help_recipe(self):
        print("\n\trecipe [name]\n\nCreate a new recipe or load an existing one (in case a file with the same name already exists).\nSpaces and underscores are not distinguishable in the name.\n")

    def do_recipe(self, arg):
        if(utils.is_valid_filename(arg)):
            name = arg.replace(" ", "_")
            self.recipe = Recipe(name)

    def do_add(self, arg):
        """

            \tadd [name]

            Add an ingredient to the active recipe or to the local ingredient pool if no recipe is active.
            Spaces and underscores are not distinguishable in the name.

        """ 

    def do_list(self, arg):
        """List all locally saved recipes and ingredients""" 
        recipes = [f.stem for f in Path(utils.data_rec_dir).glob("*.json")]
        if(len(recipes) == 0):
            print("\nNo recipes found!")
        else:
            print("\nSaved recipes:")
            for recipe in recipes:
                print("\t-" + recipe)

        ingredients = [f.stem for f in Path(utils.data_ing_dir).glob("*.json")]
        if(len(ingredients) == 0):
            print("\nNo ingredients found!")
        else:
            print("\nSaved ingredients:")
            for ingredient in ingredients:
                print("\t-" + ingredient)
        print()

    def do_exit(self, arg):
        """Exit the REPL"""
        print("Exiting...")
        return True

    def do_quit(self, arg):
        """Exit the REPL"""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Exit the REPL with Ctrl-D"""
        return self.do_exit(arg)

    def emptyline(self):
        pass  # Do nothing on empty input

def main():
    REPL().cmdloop("Welcome to nutrinfo! Type 'help' for documentation.")

if __name__ == '__main__':
    main()

