import re

n = int(input())


for a in range(n):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)