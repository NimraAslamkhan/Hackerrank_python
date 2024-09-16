# Enter your code here. Read input from STDIN. Print output to STDOUT
M= int(input())
a=set(map(int, input().split()))
N=int(input())
b=set(map(int, input().split()))

symmetric_diff = a.symmetric_difference(b)

sorted_diff = sorted(symmetric_diff)
for element in sorted_diff:
    print(element)