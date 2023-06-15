def print_rangoli(s):
    # your code goes here
    c = s - 1
    for v in map(abs, range(c, -s, -1)):
        r = c - v
        h = map(abs, range(-r, r + 1, 1))
        u = map(lambda x: abs(x - r), h)
        f = map(lambda x: chr(97 + c - x), u)
        print("-".join(list(f)).center(4 * (c) + 1, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
