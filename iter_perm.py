
from itertools import permutations

s, k = input().split()

r = sorted(list(permutations(s, int(k))))

print("\n".join("".join(i) for i in r))

    


