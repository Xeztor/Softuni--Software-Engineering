cards_given = input()

list_cards = cards_given.split()
team_a = list(range(1, 12))
team_b = list(range(1, 12))

for i in range(len(list_cards)):
    crnt_list = list_cards[i].split("-")
    if len(team_a) < 7 or len(team_b) < 7:
        break
    if crnt_list[0] == "A":
        if int(crnt_list[1]) in team_a:
            team_a.remove(int(crnt_list[1]))
    elif crnt_list[0] == "B":
        if int(crnt_list[1]) in team_b:
            team_b.remove(int(crnt_list[1]))

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
