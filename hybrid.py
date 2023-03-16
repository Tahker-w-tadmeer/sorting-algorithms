import merge
import selection


def sort(arr, threshold=10):
    sort_implementation(arr, 0, len(arr) - 1, threshold)


def sort_implementation(arr, first, last, threshold):
    if last - first <= threshold:
        selection.sort_implementation(arr, first, last)
    elif first < last:
        mid = (first + last) // 2
        sort_implementation(arr, first, mid, threshold)
        sort_implementation(arr, mid + 1, last, threshold)
        merge.merge(arr, first, mid, last)
