def chr_print(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


start = input()
stop = input()

chr_print(start, stop)
