from collections import deque

stations = int(input())
stations_data = {}

petrol_distance = [list(map(int, input().split())) for _ in range(stations)]

deque_stations = deque(petrol_distance)
succeeded_circle = []

for i in range(stations):
    fuel_tank = 0
    stations_testing = deque_stations.copy()
    first_station = stations_testing[0]

    while stations_testing and fuel_tank + stations_testing[0][0] >= stations_testing[0][1]:
        fuel_tank += stations_testing[0][0] - stations_testing[0][1]
        stations_testing.popleft()

    if not stations_testing:
        print(i)
        break

    deque_stations.append(deque_stations.popleft())




# from collections import deque
#
# n = int(input())
#
# stations = deque([])
#
# for _ in range(n):
#     stations.append(input())
#
# for big_circle_iteration in range(n):
#     is_valid = True
#     tank_petrol = 0
#     for small_circle_iteration in range(n):
#         current_station = stations[big_circle_iteration]
#
#         petrol, distance_to_next_station = current_station.split()
#         petrol = int(petrol)
#         distance_to_next_station = int(distance_to_next_station)
#         tank_petrol += petrol
#
#         if tank_petrol >= distance_to_next_station:
#             tank_petrol -= distance_to_next_station
#             stations.append(stations.popleft())
#         else:
#             is_valid = False
#             break
#     if is_valid:
#         print(big_circle_iteration)
#         break