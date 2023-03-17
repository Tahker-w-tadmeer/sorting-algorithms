import quick


def find_kth_smallest_element_imp(arr, first, last, k):
    if first < last:
        pivot = quick.randomized_partitioning(arr, first, last)
        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            return find_kth_smallest_element_imp(arr, first, pivot - 1, k)
        else:
            return find_kth_smallest_element_imp(arr, pivot - 1, last, k)


def find_smallest(arr, k):
    return find_kth_smallest_element_imp(arr, 0, len(arr) - 1, k)

