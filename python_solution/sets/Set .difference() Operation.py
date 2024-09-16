# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())  
english_subscribers = set(map(int, input().split()))  
m = int(input())  
french_subscribers = set(map(int, input().split()))  

only_english_subscribers = english_subscribers.difference(french_subscribers)


print(len(only_english_subscribers))