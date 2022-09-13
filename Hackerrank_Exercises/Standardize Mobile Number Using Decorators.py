def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            crnt_num = list(l[i])
            crnt_num = crnt_num[-10:]
            crnt_num.insert(5, ' ')
            crnt_num.insert(0, '+91 ')
            l[i] = ''.join(crnt_num)

        ret = f(l)
        return ret
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


l = [input() for _ in range(int(input()))]
sort_phone(l)
