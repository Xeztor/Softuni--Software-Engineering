n = int(input())
integer_list = map(int, input().split())

my_tp = tuple(integer_list)
print(hash(my_tp))
