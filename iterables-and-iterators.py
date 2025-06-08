import itertools
import math

def minion_game_probability(n, letters, k):
  
    a_count = letters.count('a')
    

    total_combinations = math.comb(n, k)
    
    
    non_a_combinations = math.comb(n - a_count, k) if n - a_count >= k else 0
    

    combinations_with_a = total_combinations - non_a_combinations
    

    probability = combinations_with_a / total_combinations
    
    return round(probability, 4)


n = int(input())
letters = input().split()
k = int(input())

print(minion_game_probability(n, letters, k))
