
def sort(array):
    _sort(array, 0, len(array) - 1)


def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    len_right = len(right_arr)
    len_left = len(left_arr)
    i = 0
    j = 0
    k = left
    while i < len_left and j < len_right:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def _sort(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        _sort(arr, first, mid)
        _sort(arr, mid + 1, last)
        merge(arr, first, mid, last)
