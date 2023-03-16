import quick


def find_kth_smallest_element_imp(arr, first, last, k):
    if first < last:
        pivot_index = quick.randomized_partitioning(arr, first, last)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return find_kth_smallest_element_imp(arr, first, pivot_index - 1, k)
        else:
            return find_kth_smallest_element_imp(arr, pivot_index + 1, last, k)


def find_kth_element(arr, k):
    return find_kth_smallest_element_imp(arr, 0, len(arr) - 1, k)

