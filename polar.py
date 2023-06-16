# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
from cmath import phase

c = complex(input())
r = sqrt(abs(c.real) ** 2 + abs(c.imag) ** 2)
phi = phase(c)

print(r)
print(phi)