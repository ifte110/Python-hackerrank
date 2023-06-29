from collections import OrderedDict

n = int(input())

ledger =  OrderedDict()

for i in range (n):
    name, price = input().rsplit(" ",1)
    ledger[name] = ledger.get(name,0)
    ledger[name] += int(price)


for k, v in ledger.items():
    print(k,v)

print(ledger)



