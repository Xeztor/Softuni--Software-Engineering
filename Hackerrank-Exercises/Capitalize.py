import os
def solve(s):
    check = s.replace(' ', '')
    if check.isalpha():
        return s.title()
    else:
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = s[i].capitalize()

        return ' '.join(s)


fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()
