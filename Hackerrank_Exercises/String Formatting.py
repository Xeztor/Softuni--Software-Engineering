def print_formatted(n):
    width = len(bin(n).replace('0b', ''))

    for i in range(1, n + 1):
        bin_n = bin(i).replace('0b', '')
        oct_i = oct(i).replace('0o', '')
        hex_i = hex(i).replace('0x', '')
        hex_i = hex_i.upper()
        print(str(i).rjust(width), oct_i.rjust(width), hex_i.rjust(width), bin_n.rjust(width))


n = int(input())
print_formatted(n)