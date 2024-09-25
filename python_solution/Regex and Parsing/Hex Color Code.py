# Enter your code here. Read input from STDIN. Print output to STDOUT

import re



N = int(input())
for _ in range(N):
    line = input()
    codes = [j for j in re.findall(r'[\s:](#[a-f\d]{6}|#[a-f\d]{3})[\s:),;]', line, re.I)]
  
    for code in codes:
        print (code)
