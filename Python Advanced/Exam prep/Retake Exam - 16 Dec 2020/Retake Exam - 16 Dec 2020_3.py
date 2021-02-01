def get_magic_triangle(n):
    pascal_triangle = []
    for i in range(n):
        if i == 0:
            pascal_triangle.append([1])
        elif i == 1:
            pascal_triangle.append([1, 1])
        else:
            crnt_line = []
            for j in range(len(pascal_triangle[-1]) + 1):
                if j == 0 or j == len(pascal_triangle[-1]):
                    crnt_line.append(1)
                else:
                    crnt_line.append(pascal_triangle[i - 1][j-1] + pascal_triangle[i - 1][j])

            pascal_triangle.append(crnt_line)

    return pascal_triangle


# print(get_magic_triangle(int(input())))

