import numpy as np


N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])


min_result = np.min(arr, axis=1)


max_of_min = np.max(min_result)

print(max_of_min)