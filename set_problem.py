'''
Task

You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints

0 < n < 20
0 < N < 20

Output Format

Print the sum of the elements of set  on a single line.

Sample Input

'''



def set_operations(s, N):
    """
    Perform a series of operations on the given set `s` based on user input.

    Parameters:
    s (set): A set of integers.
    N (int): The number of operations to be performed.

    Returns:
    int: The sum of the remaining elements in the set after performing all operations.
    """
    for i in range(0, N):  # Loop through the number of operations
        cmd = list(input().split())  # Read input and split into a list
        if cmd[0] == 'pop':  
            s.pop()  # Remove an arbitrary element from the set (raises KeyError if the set is empty)
        elif cmd[0] == 'remove':
            try:
                s.remove(int(cmd[1]))  # Remove the specified element (raises KeyError if element not found)
            except KeyError:
                pass  # Ignore the error if the element is not present
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))  # Remove the specified element (does nothing if element is not found)

    return sum(s)  # Return the sum of the remaining elements in the set


if __name__ == '__main__':
    n = int(input())  # Read the number of elements in the set
    s = set(map(int, input().split()))  # Read the set elements from input
    N = int(input())  # Read the number of operations
    print(set_operations(s, N))  # Execute operations and print the resulting sum
