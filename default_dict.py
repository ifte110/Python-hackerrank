# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int,input().split())

a = defaultdict(list)

l = []

for t in range(n):
    a[input()].append(t+1)

for s in range (m):
    l.append(input())

for i in l:
    if i in a.keys():
        print(*a[i])
    else:
        print(-1)