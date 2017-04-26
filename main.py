import ui
import tags
import data_manager
import sys
import copy


def choose():
    table, titles = data_manager.get_table_from_file("tags.csv")
    inputs = ui.get_inputs(["Please enter a number"], "")
    option = inputs[0]
    if option == "1":
        ui.print_table(table, titles)
    elif option == "2":
        nr_of_tags = tags.count_tags_group_by_name(table)
        ui.print_table(nr_of_tags, ["tag", "#"])
    elif option == "3":
        table_copy = copy.deepcopy(table)
        filter_tags = ui.ask_tags()
        triple_tags = tags.get_triple_tags(filter_tags)
        if triple_tags != []:
            table_copy = tags.filter_table(table_copy, triple_tags)
            filter_tags = list(set(filter_tags)-set(triple_tags))
            if filter_tags != []:
                table_copy = tags.make_simple_tags(table_copy)
                table_copy = tags.filter_table(table_copy, filter_tags)
            id_list = [x[0] for x in table_copy]
            ui.print_table(list(filter(lambda x: x[0] in set(id_list), table)), titles)
        else:
            table_copy = tags.make_simple_tags(table_copy)
            table_copy = tags.filter_table(table, filter_tags)
            id_list = [x[0] for x in table_copy]
            ui.print_table(list(filter(lambda x: x[0] in set(id_list), table)), titles)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    MAIN_MENU_OPT = ["Show all",
                     "Count tags",
                     "Filter by tags"]
    ui.print_menu("Main menu", MAIN_MENU_OPT, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)

if __name__ == '__main__':
    main()