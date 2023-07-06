from collections import Counter

n = int(input())

words = [input() for a in range(n)]

results = Counter(words)

print(len(results))
print(*results.values())