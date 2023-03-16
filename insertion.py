def sort(arr):
    n = len(arr)
    for i in range(1, n):
        index = i

        while index > 0 and arr[index - 1] > arr[index]:
            arr[index - 1], arr[index] = arr[index], arr[index - 1]
            index -= 1
