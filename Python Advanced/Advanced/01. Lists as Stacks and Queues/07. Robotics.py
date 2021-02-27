from datetime import timedelta
from collections import deque


def str_td(td):
    s = str(td).split(", ", 1)
    a = s[-1]
    if a[1] == ':':
        a = "0" + a
    s2 = s[:-1] + [a]
    return ", ".join(s2)


robots = input().split(';')
robots_data = {name: int(process_time) for name, process_time in [robot.split('-') for robot in robots]}

hours, mins, secs = list(map(int, input().split(':')))
time = timedelta(hours=hours, minutes=mins, seconds=secs)

line_queue = deque()

product = input()
while not product == 'End':
    line_queue.append(product)
    product = input()

working_robots = {name: 0 for name in robots_data}

while line_queue:
    time += timedelta(seconds=1)
    if time.days > 0:
        time -= timedelta(days=1)
    for name, val in working_robots.items():
        if val == 0:
            product = line_queue.popleft()
            working_robots[name] = robots_data[name]
            print(f'{name} - {product} [{str_td(time)}]')
            break

    for name in working_robots:
        if not working_robots[name] == 0:
            working_robots[name] -= 1

    if all([val for key, val in working_robots.items()]) and line_queue:
        line_queue.append(line_queue.popleft())

