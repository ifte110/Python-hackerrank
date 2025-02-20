for i in range(int(input())):  # Loop through the number of test cases
    l = int(input())  # Read the length of the list
    left, right = 0, -1  # Pointers to track the leftmost and rightmost elements
    ls = list(map(int, input().split()))  # Read the list of integers
    prev = 0  # Variable to store the last removed element

    # Iterate through the list length times to simulate removing elements
    for k in range(l):
        ind = 0  # Initialize index of the element to be removed

        # Determine which side (left or right) has the larger element
        if ls[left] > ls[right]:
            ind = left  # Choose the leftmost element
        elif ls[right] > ls[left]:
            ind = right  # Choose the rightmost element
        else:
            ind = left  # If equal, default to the leftmost element

        # Check if the chosen element can be removed according to the conditions
        if (ls[ind] <= prev) or (prev == 0):
            prev = ls[ind]  # Update the last removed element
            ls.pop(ind)  # Remove the chosen element

    # If the list is empty after the process, print "Yes", otherwise print "No"
    if ls == []:
        print("Yes")
    else:
        print("No")
