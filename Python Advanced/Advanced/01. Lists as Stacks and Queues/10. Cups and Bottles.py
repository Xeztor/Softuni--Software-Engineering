from collections import deque

cups = deque(list(map(int, input().split())))
cups_count = len(cups)

bottles_stack = list(map(int, input().split()))
waste = 0

while cups and bottles_stack:
    bottle = bottles_stack.pop()
    cups[0] -= bottle
    if cups[0] <= 0:
        waste += abs(cups[0])
        cups.popleft()

bottles_stack_rev = [bottles_stack.pop() for _ in range(len(bottles_stack))]
if bottles_stack_rev:
    print(f"Bottles:", *bottles_stack_rev)

if cups:
    print(f"Cups:", *cups)

print(f"Wasted litters of water: {waste}")

