first = input().split()
second = input().split()
third = input().split()


def check_row(row1, row2, row3):
    matches = []
    if len(set(row1)) == 1 and not row1[0] == 0:
        matches.append(row1[0])
    if len(set(row2)) == 1 and not row2[0] == 0:
        matches.append(row2[0])
    if len(set(row3)) == 1 and not row3[0] == 0:
        matches.append(row3[0])
    return matches


def check_column(line1, line2, line3):
    matches = []
    column1 = [line1[0], line2[0], line3[0]]
    column2 = [line1[1], line2[1], line3[1]]
    column3 = [line1[2], line2[2], line3[2]]
    if len(set(column1)) == 1 and not column1[0] == 0:
        matches.append(column1[0])
    if len(set(column2)) == 1 and not column2[1] == 0:
        matches.append(column2[0])
    if len(set(column3)) == 1 and not column3[2] == 0:
        matches.append(column3[0])
    return matches


def check_diagonal(line1, line2, line3):
    first_diagonal = [line1[0], line2[1], line3[2]]
    second_diagonal = [line1[2], line2[1], line3[0]]
    if len(set(first_diagonal)) == 1 and not line1[0] == 0:
        return line1[0]
    elif len(set(second_diagonal)) == 1 and not line1[2] == 0:
        return line1[2]


def check():
    if not check_row(first, second, third) is None or \
            not check_column(first, second, third) is None or \
            not check_diagonal(first, second, third) is None:
        if ("1" in check_column(first, second, third) and
                "2" in check_column(first, second, third)) or \
                ("1" in check_row(first, second, third) and
                 "2" in check_row(first, second, third)):
            return 12
        if "1" in check_row(first, second, third) or \
                "1" in check_column(first, second, third) or \
                check_diagonal(first, second, third) == "1":
            return 1
        if "2" in check_row(first, second, third) or \
                "2" in check_column(first, second, third) or \
                check_diagonal(first, second, third) == "2":
            return 2


if check() == 12:
    print("Draw!")
elif check() == 1:
    print("First player won")
elif check() == 2:
    print("Second player won")
else:
    print("Draw!")
