n = list(input())

result = []
for i in range(len(n)):
    if n[i].isupper():
        result.insert(i, i)

print(result)