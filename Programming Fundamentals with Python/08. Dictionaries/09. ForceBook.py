class ForceBook:
    def __init__(self):
        self.users_data = {}

    def add_check_user(self, user, side):
        if user not in self.users_data:
            self.users_data[user] = side

    def move_add_user(self, user, new_side):
        self.users_data[user] = new_side
        print(f'{user} joins the {new_side} side!')

    def status(self):
        sides = {side: [user for user in self.users_data if self.users_data[user] == side] for side in self.users_data.values()}
        sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))
        for side, users in sides.items():
            print(f'Side: {side}, Members: {len(users)}')
            if users:
                for user in sorted(users):
                    print(f'! {user}')


force_book = ForceBook()

data_given = input()
while 'Lumpawaroo' not in data_given:
    if '|' in data_given:
        side, username = data_given.split(' | ')
        force_book.add_check_user(username, side)
    elif '->' in data_given:
        username, side = data_given.split(' -> ')
        force_book.move_add_user(username, side)

    data_given = input()

force_book.status()
