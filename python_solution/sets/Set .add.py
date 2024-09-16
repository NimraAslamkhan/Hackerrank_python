# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())

country_stamps = set()

for _ in range (n):
    country_name=input().strip()
    country_stamps.add(country_name)
    
print(len(country_stamps))
    