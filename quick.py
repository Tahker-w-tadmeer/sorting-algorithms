import random


def sort(array):
    sort_implementation(array, 0, len(array)-1)


def select_random(first, last):
    return random.randint(first, last)


def randomized_partitioning(array, first, last):
    pivot = select_random(first, last)
    array[pivot], array[first] = array[first], array[pivot]
    pivot = first

    i = first + 1
    for j in range(first + 1, last + 1):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[first], array[i - 1] = array[i - 1], array[first]

    return i - 1


def sort_implementation(array, first, last):
    if first < last:
        pivot = randomized_partitioning(array, first, last)
        sort_implementation(array, first, pivot - 1)
        sort_implementation(array, pivot + 1, last)
