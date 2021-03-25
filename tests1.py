class Song:
    def __init__(self, name, lenght):
        self.name = name
        self.lenght = lenght

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.name == other.name and \
                    self.lenght == other.lenght


songs = [
    Song('reality', 3.14),
    Song('blueberry', 42),
    Song('shook ones', 58),
    Song('new york, new york', 30),
    Song('candy shop', 20),
]
print(songs)
songs.remove(Song('reality', 3.14))
print(songs)

# print(Song('blueberry', 42) in songs)
# for song in songs:
#     if song == Song('reality'):
#         print('match')

