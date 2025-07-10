from tabulate import tabulate

data_dir = sys.path[0] + "/data/"
if(not os.path.isdir(data_dir)):
    os.mkdir(data_dir)

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
