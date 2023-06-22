from collections import namedtuple

n = int(input()) 
student_list = namedtuple('student', input().split())
t = 0

for i in range(n):
    s = student_list(*input().split())
    t =  t + int(s.MARKS)

print(round(t/n,2))


"""

from collections import namedtuple

n = int(input())
a = namedtuple('A', input().split())

print(sum([float(a(*input().split()).MARKS) for _ in range(n)])/n)

"""