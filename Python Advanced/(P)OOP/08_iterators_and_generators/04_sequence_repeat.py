class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterations = 0
        self.seq_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number:
            raise StopIteration

        self.iterations += 1
        res = self.get_letter()
        return res

    def get_letter(self):
        if self.seq_index > len(self.sequence) - 1:
            self.seq_index = 0

        res_i = self.sequence[self.seq_index]
        self.seq_index += 1
        return res_i


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
