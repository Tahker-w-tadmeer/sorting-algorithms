def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        index = i

        while index > 0 and arr[index - 1] > arr[index]:
            temp = arr[index - 1]
            arr[index - 1] = arr[index]
            arr[index] = temp
            index = index - 1
    i+=1
    print(arr)


def main ():
    array_trial=[11,12,13,5,6]
    insertion_sort(array_trial)


main()