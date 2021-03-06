import collections  # for Counter in count_tags_group_by_name()


def count_tags_group_by_name(table):
    """
    Counts how many tags are in the table, grouped by their names.
    Returns a table in it tags & numbers
    """
    list_of_tags = []
    for row in table:
        list_of_tags.extend(row[1].split(", "))
    dict_of_tags = collections.Counter(list_of_tags)
    nr_of_tags = [[key, str(value)] for key, value in dict_of_tags.items()]
    return nr_of_tags


def get_triple_tags(list_of_tags):
    """
    Returns the triple tags from a list.
    e.g. "lvl:8.oszt=könnyű"
    """
    return list(filter(lambda x: x.startswith("lvl:"), list_of_tags))


def filter_table(table, filter_tags):
    """
    Filters a table by given tags.
    Args:
        - table: list of lists
        - filter_tags: list of strings
    """
    return list(filter(lambda x: set(filter_tags) - set(x[1].split(", ")) == set(), table))


def make_simple_tags(table):
    """
    Splits the triplle tags in the table for two simple tags.
    e.g.: "lvl:8.oszt=könnyű" --> "8.oszt", "könnyű"
    Returns the table
    """
    for i, line in enumerate(table):
        triple_tags = get_triple_tags(line[1].split(", "))
        for tag in triple_tags:
            line[1] += ", " + tag[4:tag.find("=")] + ", " + tag[tag.find("=")+1:]
        table[i][1] = line[1]
    return table


def main():
    pass

if __name__ == '__main__':
    main()