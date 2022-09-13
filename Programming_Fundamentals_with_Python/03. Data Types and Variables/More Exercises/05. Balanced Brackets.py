lines = int(input())

is_balanced = True
is_opening = False

for i in range(1, lines + 1):
    s = input()
    if s == ")" and not is_opening:
        is_balanced = False
    elif s == "(":
        is_opening = True
    elif s == ")" and is_opening:
        is_opening = False

if is_balanced and not is_opening:
    print("BALANCED")
else:
    print("UNBALANCED")