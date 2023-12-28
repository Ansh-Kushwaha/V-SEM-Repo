import sys

n = len(sys.argv)
print("Number of arguments:", n)
print("Name of python script:", sys.argv[0])
print("Other arguments:")
for i in range(1, n):
    print(sys.argv[i])
