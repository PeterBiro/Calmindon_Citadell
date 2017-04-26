def print_menu(title, list_options, exit_message):
    """
    Generates a menu with options.
    @title: string - title of the menu
    @list_options: list of strings - the options in the menu
    @exit_message: string - the last option with (0) (example: "Back to main menu")
    """
    print("\n", title, "\n")
    for index, option in enumerate(list_options):
        print(" ({0}) {1}".format(index+1, option))
    print(" (0)", exit_message)


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        print(label, end="")
        answer = input(": ")
        inputs.append(answer)
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("Error: ", message)


def get_col_width(table, titles):
    """
    Searches for max col widths in table and titles and returns them in a list.
    """
    result = []
    for col in titles:
        result.append(len(col))
    for line in table:
        for i, col in enumerate(line):
            if len(col) > result[i]:
                result[i] = len(col)
    return result


def make_border(column_widths, b_type):
    """
    Concatenates box-drawing lines for first/middle/last line.
    Args:
        - column_widths: list of numbers
        - b_type: string "first", "middle" or "last"
    Returns:
        line: string
    """
    b_chars = {"first": ("┌", "─", "┬", "┐"), "middle": ("├", "─", "┼", "┤"), "last": ("└", "─", "┴", "┘")}
    line = b_chars[b_type][0]
    for col_len in column_widths:
        line += b_chars[b_type][1]*col_len + b_chars[b_type][2]
    line = line[:-1] + b_chars[b_type][3]
    return line


def print_table(table, titles):
    """
    Draws a table.
    Args:
        - table: list of lists
        - titles: list of strings
    """
    column_widths = get_col_width(table, titles)
    first_border = make_border(column_widths, "first")
    middle_border = make_border(column_widths, "middle")
    last_border = make_border(column_widths, "last")

    print(first_border)
    print("│", end="")
    for i, head in enumerate(titles):
        print("{: ^{}}".format(head, column_widths[i]), end="")
        print("│", end="")
    print()
    for line in table:
        print(middle_border)
        print("│", end="")
        for i, item in enumerate(line):
            print("{: ^{}}".format(item, column_widths[i]) + "│", end="")
        print()
    print(last_border)


def ask_tags():
    """
    Asks the user for a list of tags. Returns them in a list.
    """
    answer = input("Milyen tagekre kessek? (többet vesszővel elválasztva adhatsz meg)")
    result = answer.split(",")
    return [x.strip() for x in result]


def main():
    pass


if __name__ == '__main__':
    main()