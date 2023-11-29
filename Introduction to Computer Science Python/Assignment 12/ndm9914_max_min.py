def find_max(num_list):
    """
    Finds the highest number in a list of numbers

    :param:
        num_list: list of integers or float values

    :returns:
        The highest number in the list
    """
    # Ensures input is not empty
    if not num_list:
        raise ValueError("Please input numbers in your list.")
    # Base case
    if len(num_list) == 1:
        return num_list[0]
    # Recursive case
    list_half1 = num_list[:len(num_list)//2]
    list_half2 = num_list[len(num_list)//2:]
    max1 = find_max(list_half1)
    max2 = find_max(list_half2)
    return max1 if max1 > max2 else max2


def find_min(num_list):
    """
    Finds the lowest number in a list of numbers

    :param:
        num_list: list of integers or float values

    :returns:
        The lowest number in the list
    """
    # Ensures input is not empty
    if not num_list:
        raise ValueError("Please input numbers in your list.")
    # Base case
    if len(num_list) == 1:
        return num_list[0]
    # Recursive case
    list_half1 = num_list[:len(num_list)//2]
    list_half2 = num_list[len(num_list)//2:]
    min1 = find_min(list_half1)
    min2 = find_min(list_half2)
    return min1 if min1 < min2 else min2


