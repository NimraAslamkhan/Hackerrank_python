# Enter your code here. Read input from STDIN. Print output to STDOUT


T = int(input())


for _ in range(T):

    a_size = int(input())  
    A = set(map(int, input().split()))  
    b_size = int(input())  
    B = set(map(int, input().split()))  
    
   
    print(A.issubset(B))
