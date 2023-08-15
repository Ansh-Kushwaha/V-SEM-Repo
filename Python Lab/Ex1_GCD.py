def gcd(a, b): # Euler's GCD
  if a == 0:
    return b
  
  return gcd(b % a, a)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The gcd of", x, ",", y, "is:", gcd(x, y))