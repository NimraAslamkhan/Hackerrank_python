# Enter your code here. Read input from STDIN. Print output to 
import re


def is_float(string):
    try:
        
        float_val = float(string)
        
        
        if string.count('.') == 1 and re.search(r'\d', string.split('.')[1]):
            return True
        else:
            return False
    except ValueError:
        
        return False


n = int(input())


for _ in range(n):
    s = input().strip()  
    print(is_float(s))


