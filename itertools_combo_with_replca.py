from itertools import combinations_with_replacement as pp

s , k = input().split(" ")

s = sorted(s)
k = int(k)

b = list(pp(s,k))
result = ["".join(a) for a in b]
for c in result:
    print(c)