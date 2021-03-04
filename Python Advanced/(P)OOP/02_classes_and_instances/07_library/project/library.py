class Library:
    user_records = []
    books_available = {}
    rented_books = {}
    all_rented_books = {}

    def add_user(self, user):
        user_ids = self.get_users_ids()
        if user.user_id in user_ids:
            return f"User with id = {user.user_id} already registered in the library!"

        Library.user_records.append(user)

    def remove_user(self, user):
        if user not in Library.user_records:
            return "We could not find such user to remove!"

        Library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        user_ids = self.get_users_ids()
        if user_id not in user_ids:
            return f"There is no user with id = {user_id}!"

        user = self.get_user_by_attr(user_id=user_id)
        if user:
            if user.username == new_username:
                return f"Please check again the provided username -" \
                       f" it should be different than the username used so far!"

            self.update_rented_books_username_for_user(user, new_username)
            user.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

    def get_users_ids(self):
        return [user.user_id for user in Library.user_records]

    def get_user_by_attr(self, username=None, user_id=None):
        if user_id:
            for user in Library.user_records:
                if user.user_id == user_id:
                    return user
        elif username:
            for user in Library.user_records:
                if user.username == username:
                    return user

    def update_rented_books_username_for_user(self, user, new_username):
        if user.username not in Library.rented_books:
            return

        Library.rented_books[new_username] = Library.rented_books.pop(user.username)
