phonebook = {}

cmd = input()
while not cmd.isdigit():
    name, phone = cmd.split('-')
    phonebook[name] = phone
    cmd = input()

queries = int(cmd)
for _ in range(queries):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')

