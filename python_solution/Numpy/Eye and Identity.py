import numpy as np

n,m=np.array(input().split(),int)
np.set_printoptions(legacy='1.13')
print(np.eye(n,m))