import merge
import quick
import heap
import time
import random
import insertion
import hybrid
import selection
import threading

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
]


def add_data(algorithm, name):
    for i in range(len(arrays)):
        arr = arrays[i].copy()
        m = 1_000
        start = time.time()
        algorithm.sort(arr)
        end = time.time()
        time_in_millisecond = (end-start) * m
        length_of_array = len(arr)

        with open('time.txt', 'a') as file:
            file.write(name)
            file.write("\nLength: " + "{:,}".format(length_of_array))
            file.write("\nTime in millis: " + str(time_in_millisecond) + "\n\n")


open("time.txt", "w").close()
mergeThread = threading.Thread(target=add_data, args=(merge, "Merge"))
mergeThread.start()
heapThread = threading.Thread(target=add_data, args=(heap, "Heap"))
heapThread.start()
quickThread = threading.Thread(target=add_data, args=(quick, "Quick"))
quickThread.start()
hybridThread = threading.Thread(target=add_data, args=(hybrid, "Hybrid"))
hybridThread.start()
selectionThread = threading.Thread(target=add_data, args=(selection, "Selection"))
selectionThread.start()
insertionThread = threading.Thread(target=add_data, args=(insertion, "Insertion"))
insertionThread.start()
