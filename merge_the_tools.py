import textwrap

def merge_the_tools(string, n):
    # Calculate the length of each substring
    substring_length = n
    # Split the string into substrings
    substrings = textwrap.wrap(string, substring_length)

    result_list = []
    for string in substrings:
        unique_chars = []
        for char in string:
            if char not in unique_chars:
                unique_chars.append(char)
        unique_string = ''.join(unique_chars)
        result_list.append(unique_string)
    
    print('\n'.join(result_list))
    print(unique_chars)
    print(unique_string)


    """
    def merge_the_tools(string, k):
    result = ""
    for i, c in enumerate(string, 1):
        if not c in result:
            result += c
        if i%k==0:
            print(result)
            result = ""
    
    best solution
    """



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)