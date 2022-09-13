N = int(input())

l = []
for _ in range(N):
    cmd, *args = input().split()
    args = list(map(int, args))
    if cmd == 'append':
        l.append(args.pop())
    elif cmd == 'remove':
        l.remove(args.pop())
    elif cmd == 'pop':
        l.pop()
    elif cmd == 'sort':
        l.sort()
    elif cmd == 'print':
        print(l)
    elif cmd == 'reverse':
        l.reverse()
    elif cmd == 'insert':
        l.insert(int(args[0]), args[1])
