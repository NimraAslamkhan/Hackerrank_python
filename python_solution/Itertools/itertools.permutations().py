# Enter your code here. Read input from STDIN. Print output to \

from itertools import permutations
input_str, k = input().split()
k = int(k)

perms = permutations(sorted(input_str), k)

for perm in perms:
    print(''.join(perm))
