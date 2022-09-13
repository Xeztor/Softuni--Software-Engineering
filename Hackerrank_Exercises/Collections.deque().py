from collections import deque

d = deque()

for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == 'append':
        d.append(args.pop())
    elif cmd == 'appendleft':
        d.appendleft(args.pop())
    elif cmd == 'pop':
        d.pop()
    elif cmd == 'popleft':
        d.popleft()

print(' '.join(d))
