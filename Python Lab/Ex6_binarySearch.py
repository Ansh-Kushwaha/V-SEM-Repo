def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 3, 4, 8, 12, 23, 45]
x = 8
idx = binarySearch(arr, x)
if (idx != -1):
    print(x, 'is present at index', idx)
else:
    print(x, 'is not present in the list.')