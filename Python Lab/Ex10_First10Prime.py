def findPrime(n):
  lst = []
  lst.append(2)

  num = 3
  while True:
    isPrime = True
    for i in range(2, int(num / 2) + 1):
      if num % i == 0:
        isPrime = False
        break
    if isPrime:
      lst.append(num)
    num += 1
    if len(lst) == n:
      return lst

n = 20
print(findPrime(n))
