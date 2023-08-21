def linearSearch(arr, x):
    for i in range (0, len(arr)):
        if arr[i] == x:
            return i

    return -1

arr = [23, 12, 45, 1, 8, 4, 3]
x = 8
idx = linearSearch(arr, x)
if (idx != -1):
    print(x, 'is present at index', idx)
else:
    print(x, 'is not present in the list.')