st_string_temp = input()
nd_string = input()

final = ""
symbol_chng = ""
changed = ""

while final != nd_string:
    for i in range(len(nd_string)):
        if st_string_temp[i] != nd_string[i]:
            symbol_chng = nd_string[i]
            changed += symbol_chng
            final = changed
            for j in range(i + 1, len(nd_string)):
                final += st_string_temp[j]
            print(final)
        else:
            changed += st_string_temp[i]
            final = changed
