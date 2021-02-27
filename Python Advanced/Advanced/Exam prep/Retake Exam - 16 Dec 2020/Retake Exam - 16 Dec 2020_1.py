from collections import deque


def female_is_valid(female_val):
    if female_val > 0:
        return True
    return False


def male_is_valid(male_val):
    if male_val > 0:
        return True
    return False


males = list(map(int, input().split()))

females = deque(list(map(int, input().split())))

matches = 0

while females:
    while males and not male_is_valid(males[-1]):
        males.pop()
    if males:
        crnt_female = females.popleft()
        if female_is_valid(crnt_female):
            if crnt_female == males[-1]:
                males.pop()
                matches += 1
            else:
                males[-1] -= 2
        else:
            continue
    else:
        break

print('Matches:', matches)
if males:
    print(f'Males left:', ', '.join(map(str, [males.pop() for _ in range(len(males))])))
else:
    print('Males left: none')

if females:
    print(f'Females left:', ', '.join(map(str, females)))
else:
    print('Females left: none')
