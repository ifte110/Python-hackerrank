n = input()
a = set(map(int,input().split()))
m = input()
b = set(map(int,input().split()))

c = sorted(a.union(b) - a.intersection(b))

for i in c:
    print(i)