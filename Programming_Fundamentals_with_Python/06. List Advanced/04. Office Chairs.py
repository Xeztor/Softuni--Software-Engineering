def chairs_left(rooms):
    free_chairs = 0
    for i in range(1, rooms + 1):
        free, people = input().split()
        free_chairs += free.count("X") - int(people)
        if int(people) > free.count("X"):
            print(f"{int(people) - free.count('X')} more chairs needed in room {i}")

    return free_chairs


n = int(input())

free_chairs_left = chairs_left(n)

if free_chairs_left >= 0:
    print(f"Game On, {free_chairs_left} free chairs left")
