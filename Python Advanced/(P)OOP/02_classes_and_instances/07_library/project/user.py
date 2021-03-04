class User:
    def __init__(self, user_id: int, username):
        self.user_id = user_id
        self.username = username
        self.books = []


    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if author not in library.books_available:
            return

        if book_name in library.all_rented_books:
            days_left = library.all_rented_books[book_name]
            return f"The book \"{book_name}\" is already rented and will be available in {days_left} days!"

        if book_name not in library.books_available[author]:
            return

        # Add record in the library rented_books
        if self.username not in library.rented_books:
            library.rented_books[self.username] = {book_name: days_to_return}
        else:
            library.rented_books[self.username][book_name] = days_to_return

        # Change books_available
        library.books_available[author].remove(book_name)
        # Add book to the User books
        self.books.append(book_name)

        library.all_rented_books[book_name] = days_to_return
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        books = sorted(self.books)
        return ', '.join(books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

