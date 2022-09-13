course = input()

data_courses = {}

while 'end' not in course:
    course_name, student = course.split(' : ')
    if course_name not in data_courses:
        data_courses[course_name] = [student]
    else:
        data_courses[course_name].append(student)

    course = input()

data_courses = dict(sorted(data_courses.items(), key=lambda x: len(x[1]), reverse=True))

for k, v in data_courses.items():
    print(f'{k}: {len(v)}')
    for name in sorted(v):
        print(f'-- {name}')
