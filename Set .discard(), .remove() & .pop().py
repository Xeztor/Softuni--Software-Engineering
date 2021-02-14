n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == 'pop':
        try:
            s.pop()
        except KeyError:
            continue
    elif cmd == 'discard':
        s.discard(int(args.pop()))
    elif cmd == 'remove':
        try:
            s.remove(int(args.pop()))
        except KeyError:
            continue

print(sum(s))
