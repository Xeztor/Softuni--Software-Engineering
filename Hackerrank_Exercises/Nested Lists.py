students_data = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students_data.append([name, score])

grades = list(set([el[1] for el in students_data]))
grades.remove(min(grades))
secondnd_min_grade = min(grades)

min_grade_studs = []

for name, grade in students_data:
    if grade == secondnd_min_grade:
        min_grade_studs.append(name)

[print(student) for student in sorted(min_grade_studs)]
