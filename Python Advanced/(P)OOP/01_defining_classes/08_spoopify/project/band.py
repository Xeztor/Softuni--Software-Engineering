class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album_obj = self.get_album_from_name(album_name)
        if album_obj:
            if not album_obj.published:
                self.albums.remove(album_obj)
                return f"Album {album_name} has been removed."
            else:
                return "Album has been published. It cannot be removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        albums_details = self.get_albums_details()
        return f"Band {self.name}\n" + albums_details

    def get_albums_details(self):
        albums_details = ''
        for album in self.albums:
            albums_details += album.details()
        return albums_details

    def get_album_from_name(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                return album
        else:
            return None
