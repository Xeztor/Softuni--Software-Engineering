data_users = {}

event = input()
while 'Season end' not in event:
    if '->' in event:
        player, position, skill = event.split(' -> ')
        skill = int(skill)
        if player not in data_users:
            data_users[player] = {position: skill}
        else:
            if position not in data_users[player]:
                data_users[player][position] = skill
            else:
                if skill > data_users[player][position]:
                    data_users[player][position] = skill

    else:
        attacker_1, attacker_2 = event.split(' vs ')

        if attacker_2 in data_users and attacker_1 in data_users:
            matching = any([check in data_users[attacker_2].keys() for check in data_users[attacker_1].keys()])
            if matching:
                if not sum(data_users[attacker_2].values()) == sum(data_users[attacker_1].values()):
                    if sum(data_users[attacker_1].values()) > sum(data_users[attacker_2].values()):
                        del data_users[attacker_2]
                    else:
                        del data_users[attacker_1]

    event = input()

for player, lanes in sorted(data_users.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f'{player}: {sum(lanes.values())} skill')
    for lane, skill in dict(sorted(lanes.items(), key=lambda x: (-x[1], x[0]))).items():
        print(f'- {lane} <::> {skill}')
