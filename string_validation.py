def check_string(S):
    alphanumeric = any(c.isalnum() for c in S)
    alphabetical = any(c.isalpha() for c in S)
    digits = any(c.isdigit() for c in S)
    lowercase = any(c.islower() for c in S)
    uppercase = any(c.isupper() for c in S)

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

# Read the input string
S = input()

# Call the function with the input string
check_string(S)

        

    