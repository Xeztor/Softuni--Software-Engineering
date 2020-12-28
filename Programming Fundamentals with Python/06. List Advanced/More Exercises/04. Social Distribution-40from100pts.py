def wealth_distribution(society, min_wealth):
    for i in society:
        if not i < mininum_wealth:
            if i == society[-1]:
                return "No equal distribution possible"
    for i in range(len(society)):
        while society[i] < min_wealth:
            if max(society) - 1 >= min_wealth:
                society[i] += 1
                society[society.index(max(society))] -= 1
            else:
                return "No equal distribution possible"
    return society


society_wealth = input().split(", ")
society_wealth = list(map(int, society_wealth))
mininum_wealth = int(input())
print(wealth_distribution(society_wealth, mininum_wealth))
