import math
import os
import random
import re
import sys


n = int(input())
arr = list(map(int, input().split()))

arr1 = list(set(arr))

arr1.remove(max(arr1))

print(max(arr1))

