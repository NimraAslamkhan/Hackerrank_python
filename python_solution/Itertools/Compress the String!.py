# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby


s = input()


result = [(len(list(group)), int(key)) for key, group in groupby(s)]


print(" ".join(f"({count}, {char})" for count, char in result))
