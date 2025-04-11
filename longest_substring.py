def unique_substrings(s):
    seen = {}       # Dictionary to track last index where each character was seen
    i = 0           # Start index of the current substring window
    j = 0           # Length of the longest substring found so far

    for p in range(len(s)):   # `p` is the end index of the current window
        c = s[p]              # Current character

        # If character was seen and is inside the current window
        if c in seen and seen[c] >= i:
            i = seen[c] + 1   # Move start of the window after the repeating character

        else:
            j = max(j, p - i + 1)  # Update the max length if current is longer

        seen[c] = p           # Update the latest index of the character

    return j


text = "pwwkew"
result = unique_substrings(text)
print(result)

