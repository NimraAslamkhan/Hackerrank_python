import numpy as np
n, m = map(int, input().split())
array = np.array([input().split() for _ in range(n)], int)

print (array.transpose())
print (array.flatten())
