n = int(input())
cap = int(input())

course = 0

if n % cap == 0:
    course += n // cap
else:
    course += n // cap + 1

print(course)
