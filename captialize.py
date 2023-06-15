
# Complete the solve function below.
def solve(s):
    word = s[0].upper()
    
    for i in range(1, len(s[1:]) + 1):
        if s[i-1] == ' ':
            word += s[i].upper()
        else:
            word += s[i]
        
    print(word)
    
if __name__ == '__main__':
    n = input()
    solve(n)
    