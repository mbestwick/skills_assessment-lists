"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    odd_list = list()               # creates empty list

    odd_list = [number for number in numbers if number % 2 != 0]  # loops through each number in list, checks if divisible by 2, if not adds to odd_list

    return odd_list                 # returns odd_list (list of odd numbers)


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
 
    """

    for i in range(len(items)):     # loops through indices
        print i, items[i]           # prints index then item at index


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    The returned list should not have any duplicates::
        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "cheese"],
        ...     ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        ... )
        ['bagel', 'cake', 'cheese']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    foods1_set = set(foods1)                # creates a set from foods1
    foods2_set = set(foods2)                # creates a set from foods2

    common_set = foods1_set & foods2_set    # creates a set that finds the intersection of the two new sets

    common_list = list(common_set)          # creates a list from the intersection set
    common_list.sort()                      # sorts the list alphabetically

    return common_list                      # returns the list


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       ['pickle', 'juice', 'juice']

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    return items[::2]              # returns list that is slice of input list, with step2


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    largest_list = list()               # creates empty list

    items.sort()                        # sorts input list from lowest to highest

    largest_list = [items[-i] for i in range(1, n+1)]   # in a range from 1 to n+1, appends items from the right side of input list (highest numbers)

    largest_list.sort()                 # sorts the largest_list from lowest to highest

    return largest_list                 # returns largest_list


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
