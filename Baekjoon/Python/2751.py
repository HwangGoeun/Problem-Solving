import sys
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[random.randrange(0, len(arr))]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

numbers = []
for i in range(int(sys.stdin.readline().strip())):
    numbers.append(int(sys.stdin.readline().strip()))

numbers = quick_sort(numbers)
for i in numbers:
    sys.stdout.write(str(i) + '\n')