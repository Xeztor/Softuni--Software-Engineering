lists = input().split('|')

stack = []

for l in lists:
    stack.append(l.split())

flatten = []
for _ in range(len(stack)):
    crnt_list = stack.pop()
    for digit in crnt_list:
        flatten.append(digit)

print(*flatten)

