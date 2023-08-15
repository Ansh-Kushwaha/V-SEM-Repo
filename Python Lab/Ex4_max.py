import math
def max(l):
  m = -math.inf
  for i in range(0, len(l)):
    if l[i] > m:
      m = l[i]
  return m

arr = [9, 10, 2, 4, 12, 53, 22]
print("Maximum element in", arr, "is:", max(arr))