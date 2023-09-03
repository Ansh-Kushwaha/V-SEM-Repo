def insertionSort(arr):
  n = len(arr)
  if n <= 1 :
    return
    
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key :
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

arr = [87, 34, 12, 8, 10, 50]
print("Unsorted List:", arr)
insertionSort(arr)
print("Sorted List:", arr)
