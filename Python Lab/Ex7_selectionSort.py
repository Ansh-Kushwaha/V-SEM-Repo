def selectionSort(arr):
  n = len(arr)
  if n <= 1 :
    return

  for i in range(n - 1):
    minIdx = i
    for j in range(i + 1, n):
      if arr[j] < arr[minIdx]:
        minIdx = j
    if minIdx != i:
      arr[minIdx], arr[i] = arr[i], arr[minIdx]

arr = [45, 12, 84, 36, 64]
print("Unsorted List:", arr)
selectionSort(arr)
print("Sorted List:", arr)