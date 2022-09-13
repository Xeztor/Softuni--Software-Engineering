contests = {}

new_contest = input()
while 'end of contests' not in new_contest:
    name, pw = new_contest.split(':')
    contests[name] = pw

    new_contest = input()

data_submissions = {}
users_data = {}

sumbission = input()
while 'end of submissions' not in sumbission:
    contest, password, username, pts = sumbission.split('=>')
    pts = int(pts)
    if contest in contests:
        if password == contests[contest]:
            if username not in users_data:
                users_data[username] = {contest: pts}
            else:
                if contest in users_data[username]:
                    if users_data[username][contest] < pts:
                        users_data[username][contest] = pts
                else:
                    users_data[username][contest] = pts

    sumbission = input()

winnder_user, winner_pts = max({user: sum(participations.values()) for user, participations in users_data.items()}.items(), key=lambda x: x[1])

print(f'Best candidate is {winnder_user} with total {winner_pts} points.\nRanking:')

for student, sumbmissions in dict(sorted(users_data.items(), key=lambda x: x[0])).items():
    print(f'{student}')
    for contest, pts in dict(sorted(sumbmissions.items(), key=lambda x: -x[1])).items():
        print(f'#  {contest} -> {pts}')
