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


def main():
   pass


if __name__ == '__main__':
    main()