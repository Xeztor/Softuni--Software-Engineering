class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.countdown = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.countdown < 0:
            raise StopIteration

        res = self.countdown
        self.countdown -= 1
        return res


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

