def print_rangoli(size):
    width = (size-1) * 4 + 1
    height = size * 2 - 1

    last_chr = ord('a') + (size-1)
    for i in range(height // 2 + 1):
        if i == 0 or i == height-1:
            print(f'{chr(last_chr)}'.center(width, "-"))
        else:
            str_to_center = ''
            for j in range(i):
                str_to_center += f'{chr(last_chr - j)}-'

            str_to_center += f'{chr(last_chr - i)}'

            for k in range(i - 1, -1, -1):
                str_to_center += f'-{chr(last_chr - k)}'

            print(str_to_center.center(width, '-'))

    for i in range(height // 2 - 1, -1, -1):
        str_to_center = ''
        for j in range(i):
            str_to_center += f'{chr(last_chr - j)}-'

        str_to_center += f'{chr(last_chr - i)}'

        for k in range(i - 1, -1, -1):
            str_to_center += f'-{chr(last_chr - k)}'

        print(str_to_center.center(width, '-'))


n = int(input())
print_rangoli(n)
