import random


def sort(array):
    array_length = len(array)

    if array_length <= 1:
        return

    if array_length == 2:
        if array[0] > array[1]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        return

    pivot = random.randint(0, array_length-1)
    array_less = []
    array_more = []

    for i in range(array_length):
        if array[i] < array[pivot]:
            array_less.append(array[i])
        else:
            array_more.append(array[i])

    sort(array_more)
    sort(array_less)

    i = 0
    for j in range(len(array_less)):
        array[i] = array_less[j]
        i += 1

    for j in range(len(array_more)):
        array[i] = array_more[j]
        i += 1
