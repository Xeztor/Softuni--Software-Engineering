class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        guild_members = [member.name for member in self.players]
        if player_name not in guild_members:
            return f"Player {player_name} is not in the guild."
        else:
            for member in self.players:
                if member.name == player_name:
                    self.players.remove(member)
                    return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = self.get_members_info()
        return f"Guild: {self.name}\n" + players_info

    def get_members_info(self):
        members_info = ''
        for member in self.players:
            members_info += f"{member.player_info()}"

        return members_info
