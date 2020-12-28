n = input()

string_list = list(str(n))

n_list = list(map(int, string_list))

for i in range(len(n_list)):
    print(max(n_list), end="")
    n_list.remove(max(n_list))