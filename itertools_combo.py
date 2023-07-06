from itertools import combinations

s , k = input().split(" ")

s = sorted(s)
k = int(k)

for i in range(1,k+1):
    b = sorted(list(combinations(s,i)))
    result = ["".join(a) for a in b]
    for c in result:
        print(c)






