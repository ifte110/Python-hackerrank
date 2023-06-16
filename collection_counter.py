from collections import Counter

n_shoes = int(input())
s_size = list(map(int,input().split()))
n_cus = int(input())

total_price = 0

for i in range(n_cus):
    a , b = map(int,input().split())
    if a in s_size:
        total_price = b + total_price
        s_size.remove(a)
        
print(total_price)



