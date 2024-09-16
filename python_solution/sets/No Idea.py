# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_happiness(arr, A, B):
    happiness = 0
    
    
    for item in arr:
        if item in A:
            happiness += 1  
        elif item in B:
            happiness -= 1  
    
    return happiness

if __name__ == '__main__':
    
    n, m = map(int, input().split())   
    arr = list(map(int, input().split()))  
    A = set(map(int, input().split()))  
    B = set(map(int, input().split()))  
    
    
    result = calculate_happiness(arr, A, B)
    
    
    print(result)