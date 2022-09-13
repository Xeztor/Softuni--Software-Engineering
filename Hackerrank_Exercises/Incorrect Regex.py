import re


def is_re(s):
    try:
        re.compile(rf'{s}')
        return True
    except re.error:
        return False


for _ in range(int(input())):
    if is_re(input()):
        print(True)
    else:
        print(False)
