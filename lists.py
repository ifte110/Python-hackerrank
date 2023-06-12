# initialize an empty list
my_list = []

# read the number of commands
num_commands = int(input())


#iterate through each command
for _ in range(num_commands):
    command = input().split()

    if command[0] == 'insert':
        #insert element
        position = int(command[1])
        element = int(command[2])
        my_list.insert(position, element)

    elif command[0]== "print":
        #print the list
        print(my_list)
        
    elif command[0] == "remove":
        # Remove the first occurrence of the element
        element = int(command[1])
        my_list.remove(element)
    
    elif command[0] == "append":
        # Append the element at the end of the list
        element = int(command[1])
        my_list.append(element)
    
    elif command[0] == "sort":
        # Sort the list
        my_list.sort()
    
    elif command[0] == "pop":
        # Pop the last element from the list
        my_list.pop()
    
    elif command[0] == "reverse":
        # Reverse the list
        my_list.reverse()