import merge
import quick
import heap
import insertion
import hybrid
import selection
import kpartition

unsorted_array = [5, 678, 12, 12, 12, 12, 65, 32, 14, 88, 66, 32, 88, 12, 65, 465, 123, 789, 36]
sorted_array = unsorted_array.copy()
sorted_array.sort()

array = unsorted_array.copy()
merge.sort(array)
print("Merge: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
quick.sort(array)
print("Quick: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
heap.sort(array)
print("Heap: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
insertion.sort(array)
print("Insertion: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
hybrid.sort(array)
print("Hybrid: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
selection.sort(array)
print("Selection: " + ("Sorted" if(array == sorted_array) else "NOT"))

array = unsorted_array.copy()
element1 = sorted_array[16]
element2 = kpartition.find_smallest(array, 16)
print(element1)
print(element2)
print("KPartition: " + str(element1 == element2))


array = unsorted_array.copy()
quick.randomized_partitioning(array, 0, len(array)-1)
print(array)
