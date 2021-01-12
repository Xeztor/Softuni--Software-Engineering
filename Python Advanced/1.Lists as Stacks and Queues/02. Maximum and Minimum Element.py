
PUSH = '1'
DELETE = '2'
PRINT_MAX = '3'
PRINT_MIN = '4'

queries = int(input())

stack = []

for _ in range(queries):
    query = input().split()
    if query[0] == PUSH:
        stack.append(int(query[1]))
    elif query[0] == DELETE and stack:
        stack.pop()
    elif query[0] == PRINT_MAX:
        print(max(stack))
    elif query[0] == PRINT_MIN:
        print(min(stack))

rev_stack = []
while stack:
    rev_stack.append(stack.pop())

print(', '.join(map(str, rev_stack)))

