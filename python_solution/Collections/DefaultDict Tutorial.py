# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
group_a = defaultdict(list)
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)
    
for _ in range(m):
    word_b = input().strip()
    if word_b in group_a:
        
        print(" ".join(map(str, group_a[word_b])))
    else:
        
        print(-1)