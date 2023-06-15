def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    a =[]
    for i in range(1,number+1):
        a.append(i)
    dec_numbers = [str(num) for num in a]
    oct_numbers = [str(oct(num)[2:]) for num in a]
    hex_numbers = [str(hex(num)[2:]).upper() for num in a]
    bin_numbers = [str(bin(num)[2:]) for num in a]

    for a,b,c, d in zip(dec_numbers,oct_numbers, hex_numbers, bin_numbers):
        print(a.rjust(w),b.rjust(w),c.rjust(w),d.rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)