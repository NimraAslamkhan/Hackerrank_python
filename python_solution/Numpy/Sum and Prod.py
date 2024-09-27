import numpy as np



N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])


sum_result = np.sum(arr, axis=0)


prod_result = np.prod(sum_result)


print(prod_result)