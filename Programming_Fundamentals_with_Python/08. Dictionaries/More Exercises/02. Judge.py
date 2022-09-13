contests = {}
total_points = {}

attendance = input()
while 'no more time' not in attendance:
    username, cont_name, pts = attendance.split(' -> ')
    pts = int(pts)
    if cont_name not in contests:
        contests[cont_name] = {username: pts}
    else:
        if username not in contests[cont_name]:
            contests[cont_name][username] = pts
        else:
            if contests[cont_name][username] < pts:
                contests[cont_name][username] = pts

    if username in total_points:
        if cont_name in total_points[username]:
            if pts > total_points[username][cont_name]:
                total_points[username][cont_name] = pts
        else:
            total_points[username][cont_name] = pts
    else:
        total_points[username] = {cont_name: pts}

    attendance = input()

for crnt_contest, participants in contests.items():
    print(f'{crnt_contest}: {len(participants)} participants')
    pos = 0
    for user, points in dict(sorted(participants.items(), key=lambda x: (-x[1], x[0]))).items():
        pos += 1
        print(f'{pos}. {user} <::> {points}')

print(f'Individual standings:')
pos = 0
for user, user_points in dict(sorted(total_points.items(), key=lambda x: (-sum(x[1].values()), x[0]))).items():
    pos += 1
    print(f'{pos}. {user} -> {sum(user_points.values())}')
