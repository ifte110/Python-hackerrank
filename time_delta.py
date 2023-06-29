import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    m = datetime.strptime(t1,"%a %d %b %Y %X %z")
    n = datetime.strptime(t2,"%a %d %b %Y %X %z")
    c = abs(int((m-n).total_seconds()))
    print(c)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)