expression = input()

is_balanced = True
mapper = {'{': '}', '[': ']', '(': ')'}

stack = []

for chr in expression:
    if chr in '[{(':
        stack.append(chr)
    else:
        if not stack:
            is_balanced = False
        if stack and not mapper[stack.pop()] == chr:
            is_balanced = False

if is_balanced:
    print('YES')
else:
    print('NO')