def loading_bar(loaded_perc):
    bar = []
    loaded_perc //= 10
    for i in range(loaded_perc):
        bar.append("%")
    for i in range(10 - loaded_perc):
        bar.append(".")
    return bar


n = int(input())
if n == 100:
    print(f"{n}% Complete!")
    print("[" + "".join(loading_bar(n)) + "]")
else:
    print(f"{n}%", "[" + "".join(loading_bar(n)) + "]")
    print("Still loading...")
