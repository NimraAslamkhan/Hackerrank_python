import numpy as np



n, m = map(int, input().split())


a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(n)])


print(np.add(a, b))            # Addition
print(np.subtract(a, b))       # Subtraction
print(np.multiply(a, b))       # Multiplication
print(np.floor_divide(a, b))   # Integer Division (floor division)
print(np.mod(a, b))            # Modulus
print(np.power(a, b))          # Power
