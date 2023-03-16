import merge
import selection


def sort(arr, threshold=3):
    merge_sort_implementation(arr, 0, len(arr) - 1, threshold)


def merge_sort_implementation(arr, first, last, threshold):
    if last - first <= threshold:  # starts selection sort at threshold
        selection.sort_implementation(arr, (first + last + 1)//2)
    else:
        mid = (first + last) // 2
        merge_sort_implementation(arr, first, mid, threshold)
        merge_sort_implementation(arr, mid + 1, last, threshold)
        merge.merge(arr, first, mid, last)
