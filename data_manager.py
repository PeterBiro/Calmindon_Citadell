import random  # for random table, so later it can be omitted


def generate_random_table(rows):
    TAGS = {
            "matek", "fizika", "geometria", "algebra", "analízis", "szöveges feladat",
            "teszt", "2016", "2017", "érettségi", "könnyű", "nehéz", "húbaz+", "KöMaL",
            "kinematika", "mechanika", "hőtan", "elektromágnesség", "optika", "7. osztály",
            "8. osztály", "9-10. osztály", "12. osztály", "egyetem", "fejtörő", "Pithagorasz-tétel",
            "Euler-egyenes", "Euler-tétel", "Euler-féle poliédertétel", "Euler-Fermat tétel",
            "Königsberg hídjai", "lovagok és lókötők", "Newton-törvények", "Kepler-törvények",
            "Kepler III. tv", "Jennifer Lawrence"
            }
    table = []
    for i in range(rows):
        table.append([str(i), ", ".join(random.sample(TAGS, random.randrange(1, 7)))])
    return table


def write_table_to_file(file_name, table, titles):
    with open(file_name, "w") as file:
        row = ";".join(titles)
        file.write(row + "\n")
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    titles = lines[0].replace("\n", "").split(";")
    lines = lines[1:]
    table = [element.replace("\n", "").split(";") for element in lines]
    return table, titles


def main():
    # table = generate_random_table(25)
    # write_table_to_file("tags.csv", table, ["ID", "Tags"])
    pass

if __name__ == '__main__':
    main()