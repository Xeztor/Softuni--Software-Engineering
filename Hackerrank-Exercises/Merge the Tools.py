def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        ui = list(set(string[i:i + k]))
        print(''.join(ui))


string, k = input(), int(input())
merge_the_tools(string, k)
