# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


s = input().strip()


match = re.search(r'([a-zA-Z0-9])\1', s)


if match:
    print(match.group(1))
else:
    print(-1)
