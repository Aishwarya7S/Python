# List as Array
arr = [1, 2, 3, 4]
arr.append(5)
arr.insert(2, 10)
arr.remove(3)
arr.pop()
arr.sort()
arr.reverse()
print("Array:",arr)

# Using array Module
from array import array

arr = array('i', [1, 2, 3, 4])
arr.append(5)
arr.insert(1, 10)
arr.remove(3)
arr.pop()
idx = arr.index(2)
arr.reverse()
info = arr.buffer_info()
cnt = arr.count(2)
arr.extend([6, 7])
arr.fromlist([8, 9])
lst = arr.tolist()

print("Final Array:", arr)
print("Index of 2:", idx)
print("Buffer Info:", info)
print("Count of 2:", cnt)
print("As list:", lst)
Sliced_array = arr[1:4]
print(Sliced_array)
for i in range(0, 3):
    print(arr[i], end=" ")

# NumPy Arrays
import numpy as np

arr = np.array([[1, 2], [3, 4]])

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Sum:", arr.sum())
print("Cumulative Sum:", arr.cumsum())
print("Mean:", arr.mean())
print("Product:", arr.prod())
print("Max:", arr.max())
print("Min:", arr.min())
print("Sorted Array:", np.sort(arr))
print("Where > 2:", np.where(arr > 2))
