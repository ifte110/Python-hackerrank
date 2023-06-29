n, m = map(int,input().split(' '))

a = map(int,input().split(' '))

A = set(map(int,input().split(' ')))

B = set(map(int,input().split(' ')))

prize = 0

for i in a:
    if i in A:
        prize+=1        
    if i in B:
        prize-=1

print(prize)



