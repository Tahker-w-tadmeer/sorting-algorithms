import merge
import quick
import heap
import time
import random
import insertion
import hybrid
import selection
import matplotlib.pyplot as plt
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

xMerge = []
yMerge = []

xQuick = []
yQuick = []

xInsertion = []
yInsertion = []

xSelection = []
ySelection = []

xHybrid = []
yHybrid = []

xHeap = []
yHeap = []


def add_data(algorithm, points):
    for i in range(len(arrays)):
        arr = arrays[i].copy()
        m = 1_000
        start = time.time()
        algorithm.sort(arr)
        end = time.time()
        points[1].append((end-start) * m)
        points[0].append(len(arr))


add_data(merge, [xMerge, yMerge])

add_data(quick, [xQuick, yQuick])

add_data(heap, [xHeap, yHeap])

add_data(hybrid, [xHybrid, yHybrid])

add_data(selection, [xSelection, ySelection])

add_data(insertion, [xInsertion, yInsertion])


plt.plot(xMerge, yMerge, label="Merge", markersize=8, marker='o')
plt.plot(xQuick, yQuick, label="Quick", markersize=8, marker='o')
plt.plot(xHeap, yHeap, label="Heap", markersize=8, marker='o')
plt.plot(xHybrid, yHybrid, label="Hybrid", markersize=8, marker='o')
plt.plot(xSelection, ySelection, label="Selection", markersize=8, marker='o')
plt.plot(xInsertion, yInsertion, label="Insertion", markersize=8, marker='o')


plt.xlabel('Input Size (N)')
plt.ylabel('Execution time (ms)')
plt.title("Line graph")
plt.legend()
plt.show()
