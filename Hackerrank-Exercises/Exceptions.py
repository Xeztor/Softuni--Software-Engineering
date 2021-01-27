def try_except(a, b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError as err:
        print('Error Code:', err)
    except ValueError as err:
        print('Error Code:', err)


def print_result(ll):
    print(' '.join([str(el) for el in ll if el is not None]))


for _ in range(int(input())):
    a, b = input().split()
    if try_except(a, b) is not None:
        print(int(a) // int(b))
