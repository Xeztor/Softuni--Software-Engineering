class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.name == other.name
