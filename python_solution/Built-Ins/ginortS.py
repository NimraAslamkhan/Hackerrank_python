# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()

lowercase = sorted(c for c in s if c.islower())

uppercase = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)
result = ''.join(lowercase + uppercase + odd_digits + even_digits)
print(result)
