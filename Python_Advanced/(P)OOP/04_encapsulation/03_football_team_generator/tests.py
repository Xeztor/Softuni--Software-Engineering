from project.player import Player
from project.team import Team

messi = Player('messi', 100, 100, 100, 100, 100)
team = Team('Barcelona', 10)

print(messi)
print(team.add_player(messi))
print(team.remove_player('messi'))
