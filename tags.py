import data_manager
import ui
import collections  # for Counter in count_tags_group_by_name()


def count_tags_group_by_name(table):
    """
    Counts how many tags are in the table, grouped by their names.
    Returnds a table in it tags & numbers
    """
    list_of_tags = []
    for row in table:
        list_of_tags.extend(row[1].split(", "))
    dict_of_tags = collections.Counter(list_of_tags)
    nr_of_tags = [[key, str(value)] for key, value in dict_of_tags.items()]
    return nr_of_tags


def filter_table(table, filter_tags):
    """
    Filters a table by given tags.
    Args:
        - table: list of lists
        - filter_tags: list of strings
    """
    result = list(filter(lambda x: set(filter_tags) - set(x[1].split(", ")) == set(), table))
    return result


def main():
    table, titles = data_manager.get_table_from_file("tags.csv")
    ui.print_table(table, titles)
    nr_of_tags = count_tags_group_by_name(table)
    ui.print_table(nr_of_tags, ["tag", "#"])
    filter_tags = ui.ask_tags()
    print(filter_table(table, filter_tags))
    ui.print_table(filter_table(table, filter_tags), titles)




if __name__ == '__main__':
    main()