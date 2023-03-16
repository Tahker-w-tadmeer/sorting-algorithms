import merge
import quick
import heap
import time
import random
import insertion
import hybrid
import selection

array10m = range(10_000_000)

array1k = random.sample(array10m, 1_000)
array25k = random.sample(array10m, 25_000)
array50k = random.sample(array10m, 50_000)
array100k = random.sample(array10m, 100_000)
array250k = random.sample(array10m, 250_000)
array500k = random.sample(array10m, 500_000)
array1m = random.sample(array10m, 1_000_000)

arrays = [
    array1k,
    array25k,
    array50k,
    array100k,
    array250k,
    array500k,
    array1m,
]

m = 1_000_000
for i in range(len(arrays)):
    print("Array " + str(i + 1))

    array = arrays[i].copy()
    start_time = time.time()
    merge.sort(array)
    end_time = time.time()
    print("Merge Sort: " + str((end_time-start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    quick.sort(array)
    end_time = time.time()
    print("Quick Sort: " + str((end_time-start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    heap.sort(array)
    end_time = time.time()
    print("Heap Sort: " + str((end_time-start_time) * m) + "µs")

    # array = arrays[i].copy()
    # start_time = time.time()
    # insertion.sort(array)
    # end_time = time.time()
    # print("Insertion Sort: " + str((end_time-start_time) * m) + "µs")

    # array = arrays[i].copy()
    # start_time = time.time()
    # selection.sort(array)
    # end_time = time.time()
    # print("Selection Sort: " + str((end_time-start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    hybrid.sort(array)
    end_time = time.time()
    print("Hybrid Sort: " + str((end_time-start_time) * m) + "µs")

    print()


