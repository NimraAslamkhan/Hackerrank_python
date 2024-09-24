# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


s = input().strip()


pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'


matches = re.findall(pattern, s)


if matches:
    for match in matches:
        print(match)
else:
    print(-1)