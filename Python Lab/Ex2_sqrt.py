def sqrt(n):
  x = n
  while (True):
    x1 = 0.5 * (x + (n / x))

    if (abs(x1 - x) < 0.000000001):
      return x1
    x = x1

a = int(input("Enter a number: "))
print("sqrt of", a, "=", sqrt(a))