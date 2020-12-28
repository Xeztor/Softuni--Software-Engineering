n = int(input())
students = {}

for i in range(n):
    name, grade = input(), float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

students = {k: sum(grades) / len(grades) for k, grades in students.items() if sum(grades) / len(grades) >= 4.50}

for name, grade in dict(sorted(students.items(), key=lambda x: x[1], reverse=True)).items():
    print(f'{name} -> {grade:.2f}')
