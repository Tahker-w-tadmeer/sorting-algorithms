def sort(array):
    sort_implementation(array, 0, len(array)-1)


def sort_implementation(arr, first, last):
    for i in range(first, last):
        min_index = i
        for j in range(i + 1, last + 1):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
