def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        nums = integers()
        while True:
            num = next(nums)
            yield num / 2

    def take(n, seq):
        halves_nums = seq
        res = []
        for _ in range(n):
            res.append(next(halves_nums))

        return res

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
