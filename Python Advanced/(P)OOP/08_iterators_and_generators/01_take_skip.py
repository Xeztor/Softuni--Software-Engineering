class take_skip:
    def __init__(self, skip, count):
        self.skip = skip
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.count:
            raise StopIteration

        res = self.i * self.skip
        self.i += 1
        return res


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
