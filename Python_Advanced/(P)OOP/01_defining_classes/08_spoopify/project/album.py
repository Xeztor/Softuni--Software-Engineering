class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return 'Song is already in the album.'
        elif self.published:
            return 'Cannot add songs. Album is published.'
        elif song.single:
            return f"Cannot add {song.username}. It's a single"
        else:
            if not self.is_album_empty():
                self.songs.append(song)
            else:
                self.songs = [song]
            return f"Song {song.username} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            all_song_names = self.get_song_names()
            if song_name in all_song_names:
                song = self.get_song_by_name(song_name)
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            else:
                return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        songs_details = self.get_songs_details()
        return f"Album {self.name}\n" + songs_details

    def get_song_by_name(self, song_name):
        for song in self.songs:
            if song.username == song_name:
                return song

    def get_song_names(self):
        if self.is_album_empty():
            return []
        else:
            return [song.username for song in self.songs]

    def get_songs_details(self):
        songs_details = ''
        for song in self.songs:
            songs_details += f"== {song.get_info()}"
        return songs_details

    def is_album_empty(self):
        if not self.songs:
            return True
        return False

    def __eq__(self, other):
        if isinstance(other, Album):
            return self.name == other.name
