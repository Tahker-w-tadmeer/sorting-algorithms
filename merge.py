import math


def sort(array):
    length = len(array)

    if length < 2:
        return array

    middle = math.floor(length / 2)
    left = sort(array[0:middle])
    right = sort(array[middle:])

    return _merge(left, right)


def _merge(left, right):
    len_left = len(left)
    len_right = len(right)
    i = j = 0
    merged = []

    while i < len_left and j < len_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len_left:
        merged.append(left[i])
        i += 1

    while j < len_right:
        merged.append(right[j])
        j += 1

    return merged
