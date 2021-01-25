nums = list(map(int, input().split()))

positive = list(filter(lambda x: x >= 0, nums))
negative = list(filter(lambda x: x < 0, nums))

print(f'{sum(negative)}\n{sum(positive)}')
if abs(sum(negative)) > sum(positive):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')

