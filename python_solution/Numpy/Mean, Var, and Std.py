import numpy as np


N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])


mean_result = np.mean(arr, axis=1)


var_result = np.var(arr, axis=0)


std_result = np.std(arr, axis=None)


print(mean_result)
print(var_result)
print(round(std_result, 11))  