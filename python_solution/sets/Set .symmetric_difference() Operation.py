# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())  
english_subscribers = set(map(int, input().split()))  
m = int(input()) 
french_subscribers = set(map(int, input().split()))  


either_but_not_both = english_subscribers.symmetric_difference(french_subscribers)


print(len(either_but_not_both))