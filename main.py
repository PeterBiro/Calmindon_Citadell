import ui
import tags
import data_manager
import sys

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
        filter_tags = ui.ask_tags()
        ui.print_table(tags.filter_table(table, filter_tags), titles)
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