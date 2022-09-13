from collections import OrderedDict


class OrderedDictWithDefaultInt(OrderedDict):
    def __missing__(self, key):
        value = 0
        self[key] = value
        return value


data = OrderedDictWithDefaultInt()
n = int(input())

for _ in range(n):
    word = input()
    data[word] += 1

print(len(data))
[print(occurr, end=' ') for word, occurr in data.items()]
