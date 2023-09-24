def binarySearchI(arr, x):
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

def binarySearchR(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchR(arr, low, mid - 1, x)
        else:
            return binarySearchR(arr, mid + 1, high, x)
    return -1

arr = [1, 3, 4, 8, 12, 23, 45]
x = 23
idx = binarySearchR(arr, 0, len(arr) - 1, x)
if (idx != -1):
    print(x, 'is present at index', idx)
else:
    print(x, 'is not present in the list.')