from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))

p = product(A,B)

print(*p,sep=" ")