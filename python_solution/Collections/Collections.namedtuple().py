# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())  
columns = input().split()  


Student = namedtuple('Student', columns)


marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(f"{sum(marks) / len(marks):.2f}")
