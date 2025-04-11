'''

Task : https://www.hackerrank.com/challenges/iterables-and-iterators/problem


'''


# Import the combinations function from itertools
from itertools import combinations

# Take three inputs:
# n: the length of the list
# s: the elements of the list (split into individual items)
# k: the size of each combination
n, s, k = int(input()), input().split(), int(input())

# Generate all possible combinations of 's' taken 'k' at a time
c = list(combinations(s, k))

# Print all combinations (for debugging or visualization purposes)
print(c)

# Initialize a counter to count combinations containing the letter 'a'
counter = 0

# Iterate through each combination
for item in c:
    if "a" in item:  # Check if 'a' is present in the combination
        counter += 1

# Calculate and print the proportion of combinations containing 'a'
print(counter / len(c))
