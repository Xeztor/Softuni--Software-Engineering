class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.name = name
        self.endurance = endurance
        self.sprint = sprint
        self.dribble = dribble
        self.passing = passing
        self.shooting = shooting

    def __str__(self):
        return f"Player: {self.name}\n" \
               f"Endurance: {self.endurance}\n" \
               f"Sprint: {self.sprint}\n" \
               f"Dribble: {self.dribble}\n" \
               f"Passing: {self.passing}\n" \
               f"Shooting: {self.shooting}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value: int):
        self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value: int):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value: int):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value: int):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value: str):
        self.__shooting = value
