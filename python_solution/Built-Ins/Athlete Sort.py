import math
import os
import random
import re
import sys
N, M = map(int, input().split())
athletes = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

sorted_athletes = sorted(athletes, key=lambda x: x[K])
for athlete in sorted_athletes:
    print(" ".join(map(str, athlete)))