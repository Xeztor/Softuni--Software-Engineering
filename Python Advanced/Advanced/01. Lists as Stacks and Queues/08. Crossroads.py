from collections import deque

crash = False
passed = 0
green_duration = int(input())
window_duration = int(input())

traffic = deque()

cmd = input()
while not cmd == 'END' and not crash:

    if cmd == 'green':
        green_left = green_duration
        crossroad = deque()
        while green_left > 0 and traffic:
            car_into_crossroad = traffic.popleft()
            crossroad.append(list(car_into_crossroad))
            green_left -= len(car_into_crossroad)

        time_to_cross = green_duration + window_duration
        while crossroad:
            crnt_car = crossroad.popleft()
            crossing = deque(crnt_car)
            while time_to_cross and crossing:
                crossing.popleft()
                time_to_cross -= 1
            else:
                if crossing:
                    print(f"A crash happened!\n{''.join(crnt_car)} was hit at {crossing.popleft()}.")
                    crash = True
                else:
                    passed += 1
    else:
        car_model = cmd
        traffic.append(car_model)

    cmd = input()


if not crash:
    print(f'Everyone is safe.\n{passed} total cars passed the crossroads.')


