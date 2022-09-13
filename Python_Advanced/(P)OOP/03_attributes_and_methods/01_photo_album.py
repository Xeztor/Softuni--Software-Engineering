class PhotoAlbum:
    max_photos_on_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.crnt_page = 1
        self.last_slot = 1

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    @staticmethod
    def is_page_full(page):
        return len(page) == PhotoAlbum.max_photos_on_page

    def add_photo(self, label):
        if self.is_page_full(self.photos[self.crnt_page - 1]):
            self.crnt_page += 1

        if self.crnt_page > self.pages:
            return "No more free spots"

        self.photos[self.crnt_page - 1].append(label)
        return f"{label} photo added successfully on page {self.crnt_page}" \
               f" slot {len(self.photos[self.crnt_page - 1])}"

    def display(self):
        pages_info = self.display_pages()
        return '-' * 11 + '\n' + pages_info

    def display_pages(self):
        res = ''
        for page in range(self.pages):
            line = '\n'
            if self.photos[page]:
                photos_repr = ['[]' for _ in range(len(self.photos[page]))]
                line = ' '.join(photos_repr) + '\n'
            res += line + '-' * 11 + '\n'

        return res

#
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

