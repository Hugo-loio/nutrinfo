import cmd
from pathlib import Path

import utils

class REPL(cmd.Cmd):
    prompt = ">>> "

    #def do_help(self):

    def do_list(self):
        recipes = [f.stem for f in Path(utils.data_rec_dir).glob("*.json")]
        print("\nSaved recipes:")
        for recipe in recipes:
            print("\t-" + recipe)

        ingredients = [f.stem for f in Path(utils.data_ing_dir).glob("*.json")]
        print("\nSaved ingredients:")
        for ingredient in ingredients:
            print("\t-" + ingredient)

    def do_exit(self):
        """Exit the REPL"""
        print("Exiting...")
        return True

    def do_quit(self):
        """Exit the REPL"""
        return self.do_exit(arg)

    def emptyline(self):
        pass  # Do nothing on empty input

if __name__ == '__main__':
    REPL().cmdloop("Welcome to nutrinfo! To list avaible commands type 'help'. Type 'exit' to quit.")

les)
