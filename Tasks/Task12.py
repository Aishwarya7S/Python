# Array
import array
arr = array.array('i',[1,2,3,4,5,6,7])
print(arr)
print(arr[2])
print(arr[-1])
print(len(arr))
arr.remove(6)
print(arr[1:4])
print(arr.index(5))
print(arr)
arr[1] = 13
print(arr)
arr[3] = 77
for ele in arr:
    print(ele, end = ' ')