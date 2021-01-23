strings = input().split(', ')

result = [f'{word} -> {len(word)}' for word in strings]

print(', '.join(result))
