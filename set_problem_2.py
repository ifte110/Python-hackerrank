'''

Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, 
some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
and the other set is subscribed to the French newspaper. The same student could be in both sets. 
Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Constraints

0 < Total numbers of students in college < 1000

Output Format

Output the total number of students who have at least one subscription.

Same soltuion for union, intersection, difference and symmetric between two sets

'''

def create_set(a, b):
    """
    Create a set that is the union of two given sets and return its length.

    Parameters:
    a (set): The first set of integers.
    b (set): The second set of integers.

    Returns:
    int: The number of unique elements in the union of both sets.
    """
    s = a.union(b)  # Compute the union of sets a and b
    return len(s)  # Return the number of unique elements in the union


if __name__ == '__main__':
    m = int(input())  # Read the number of elements in the first set
    a = set(map(int, input().split()))  # Read the elements of the first set
    n = int(input())  # Read the number of elements in the second set
    b = set(map(int, input().split()))  # Read the elements of the second set
    print(create_set(a, b))  # Print the number of unique elements in the union of both sets

