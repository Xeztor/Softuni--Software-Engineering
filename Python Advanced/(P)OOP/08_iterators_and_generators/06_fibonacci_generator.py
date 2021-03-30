def fibonacci():
    i = 0
    last_num = 1
    before_last_num = 1
    while True:
        if i == 0:
            yield 0
        elif i < 3:
            yield 1
        else:
            crnt = last_num + before_last_num
            before_last_num = last_num
            last_num = crnt
            yield crnt

        i += 1


generator = fibonacci()
for i in range(8):
    print(next(generator))
