# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    x=input()
    
    if re.match(r"[7,8,9]\d{9}$",x):
        print("YES")
    else:
        print("NO")