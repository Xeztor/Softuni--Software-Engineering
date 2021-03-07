class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value: str):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value: list):
        self.__players = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        asked_player = [player for player in self.players if player.name == player_name]
        if not asked_player:
            return f"Player {player_name} not found"

        asked_player = asked_player.pop()
        self.players.remove(asked_player)
        return asked_player
