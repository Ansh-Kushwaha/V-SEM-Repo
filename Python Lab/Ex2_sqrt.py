def sqrt(n):
  x = n
  if x < 0:
    raise ValueError("math domain error")
  
  if x == 0:
    return 0.0
  
  while True:
    x1 = 0.5 * (x + (n / x))

    if (abs(x1 - x) < 0.000000001):
      return x1
    x = x1

a = int(input("Enter a number: "))
print("Square root of", a, "=", sqrt(a))