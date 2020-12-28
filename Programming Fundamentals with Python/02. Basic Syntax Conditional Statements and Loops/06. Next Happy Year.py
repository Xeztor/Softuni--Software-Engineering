given = int(input())

inner_flag = True

flag = True
while flag:
    given += 1
    string_given = str(given)
    for i in range(len(string_given)-1):
        for j in range(i + 1, len(string_given)):
            if string_given[i] == string_given[j]:
                inner_flag = False
                break
        if not inner_flag:
            inner_flag = True
            break
        elif flag and i == len(string_given)-2:
            print(given)
            flag = False
            break