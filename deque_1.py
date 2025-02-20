from collections import deque  # Importing deque from the collections module

n = int(input())  # Taking an integer input for the number of operations
d = deque()  # Initializing an empty deque

# Loop through the given number of operations
for _ in range(n):
    cmd = input().split()  # Read input and split it into command and arguments
    operation = cmd[0]  # Extract the operation type

    # Perform the respective deque operation based on input
    if operation == "append":
        d.append(int(cmd[1]))  # Add element to the right end of the deque
    elif operation == "appendleft":
        d.appendleft(int(cmd[1]))  # Add element to the left end of the deque
    elif operation == "pop":
        d.pop()  # Remove element from the right end of the deque
    elif operation == "popleft":
        d.popleft()  # Remove element from the left end of the deque

# Print the deque elements separated by space
print(*d)  
