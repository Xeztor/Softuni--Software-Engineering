data = list(map(int, input().split()))

[print(data.pop(), end=" ") for _ in range(len(data))]
