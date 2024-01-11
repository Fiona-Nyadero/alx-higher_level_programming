#!/usr/bin/python3
""" find_peak function module """


def find_peak(list_of_integers):
    """
    Find a peak in lists of unsorted integers

    Args:
        list_of_integers (list): List of unsorted integers

    Returns:
        int or None: Peak element(int) or None if list is empty
    """
    if not list_of_integers:
        return None

    links, rechts = 0, len(list_of_integers) - 1

    while links < rechts:
        midpoint = (links + rechts) // 2

        if list_of_integers[midpoint] > list_of_integers[midpoint + 1]:
            rechts = midpoint
        else:
            links = midpoint + 1

    return list_of_integers[links]
