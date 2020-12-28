import operator


def person_lister(f):
    def inner(people):
        for j in people:
            j[2] = int(j[2])

        people.sort(key=operator.itemgetter(2))

        ret = [f(people[i]) for i in range(len(people))]
        return ret
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


people = [input().split() for i in range(int(input()))]
print(*name_format(people), sep='\n')