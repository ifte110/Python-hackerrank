def count_substring(string, sub_string):
    count = 0
    start = 0

    while True:
        # Find the index of the next occurrence of the substring
        index = string.find(sub_string, start)

        if index == -1:
            break

        # Update the start position for the next search
        start = index + 1
        count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)