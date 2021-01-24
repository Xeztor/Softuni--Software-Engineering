lists = input().split('|')

stack = []

for l in lists:
    ll = []
    for i in l:
        if i.isdigit():
            ll.append(int(i))
    stack.append(ll)

flatten = []
for _ in range(len(stack)):
    crnt_list = stack.pop()
    for digit in crnt_list:
        flatten.append(digit)

print(*flatten)

