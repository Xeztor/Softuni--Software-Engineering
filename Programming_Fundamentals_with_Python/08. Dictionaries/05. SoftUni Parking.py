class ParkingLot:
    def __init__(self):
        self.users = {}

    def register(self, username, license_plate):
        if username not in self.users:
            self.users[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate}')

    def unregister(self, username):
        if username in self.users:
            del self.users[username]
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')

    def status(self):
        for k, v in self.users.items():
            print(f'{k} => {v}')


n = int(input())
parking_lot = ParkingLot()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'register':
        parking_lot.register(cmd[1], cmd[2])
    elif cmd[0] == 'unregister':
        parking_lot.unregister(cmd[1])

parking_lot.status()
