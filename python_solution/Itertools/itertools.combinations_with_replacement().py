# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

input_str, k = input().split()
k = int(k)

sorted_str = sorted(input_str)
comb_with_replacement = combinations_with_replacement(sorted_str, k)

# Print each combination
for comb in comb_with_replacement:
    print(''.join(comb))
