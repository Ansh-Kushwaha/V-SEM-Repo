# Raise x to the power of n
def pow(x, n):
  if n < 0:
    return pow(1 / x, -n)
  elif n == 0:
    return 1
  elif n % 2 == 0:
    return pow(x * x, n / 2)
  else:
    return x * pow(x, n - 1)
  
a = int(input("Enter a number: "))
n = int(input("Enter the power you want to raise to: "))
print(a, "raised to the power of", n, "=", pow(a, n))