def rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    lines = []
    
def print_rangoli(size):
    
    l1=list(map(chr,range(97,123)))
    x=l1[n-1:0:-1]+l1[0:n]
    
    y=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(y,'-'))
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(y,'-'))    
 
      
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)