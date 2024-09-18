from itertools import combinations

# Input
n = int(input())  
letters = input().split()  
k = int(input())  


total_combinations = list(combinations(range(n), k))


count_with_a = sum(1 for comb in total_combinations if any(letters[i] == 'a' for i in comb))


probability = count_with_a / len(total_combinations)


print(f"{probability:.4f}")