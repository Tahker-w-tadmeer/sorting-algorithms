
def build_max_heap(array):
    n = len(array)

    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, i, n)


def heapify(array, i, n):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    largest = i

    if left_child < n and array[left_child] > array[largest]:
        largest = left_child

    if right_child < n and array[right_child] > array[largest]:
        largest = right_child

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, n)


def sort(array):
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]

        heapify(array, 0, i)

    return array
