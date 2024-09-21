# Enter your code here. Read input from STDIN. Print output to 


T = int(input())

for _ in range(T):
    a, b = input().split()
    
    try:
       
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        
        print("Error Code:", e)
    except ValueError as e:
       
        print("Error Code:", e)
