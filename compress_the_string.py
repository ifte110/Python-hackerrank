### itertool tutorial


# import itertools

# data = [100,200,200,400]

# data_ite = list(itertools.zip_longest(range(10), data))

# print(data_ite)

# groups = []
# uniquekeys = []
# data = sorted(data)
# for k, g in itertools.groupby(data):
#     groups.append(list(g))      # Store group iterator as a list
#     uniquekeys.append(k)
#     print(groups)
#     print(k)


'''
Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string (X,c) where X = number of occ of character 'c'.

1222311 -> (1, 1) (3, 2) (1, 3) (2, 1)

'''


from itertools import groupby
s=list(input())
print(list(groupby(s)))
for k,g in groupby(s):
    print(f"({len(list(g))}, {k})", end=" ")