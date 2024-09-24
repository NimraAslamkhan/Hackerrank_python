# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


s = input().strip()
k = input().strip()


matches = list(re.finditer(r'(?={})'.format(re.escape(k)), s))


if not matches:
    print((-1, -1))
else:
   
    for match in matches:
        start_idx = match.start()
        end_idx = start_idx + len(k) - 1
        print((start_idx, end_idx))