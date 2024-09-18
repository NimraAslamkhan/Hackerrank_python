from itertools import product 


# Input the two lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the Cartesian product
cartesian_product = list(product(A, B))

# Print the tuples in the required format
print(" ".join(map(str, cartesian_product)))