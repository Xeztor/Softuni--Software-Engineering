from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
marks = list(map(int, [Student(*input().split()).MARKS for _ in range(n)]))
print(f'{sum(marks)/len(marks):.2f}')
