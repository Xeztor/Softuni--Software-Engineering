import os

def create_file(file_name, content=None):
    if not content:
        with open(f'{file_name}', 'w'):
            pass
    else:
        with open(f'{file_name}', 'w') as file:
            file.write(content)


def add_to_file(file_given, content):
    try:
        with open(f'{file_given}', 'a') as file:
            file.write(content + '\n')
    except FileNotFoundError:
        create_file(file_given, content)


def replace_str_in_file(file_name, old_str, new_str):
    try:
        with open(f'{file_name}', 'r') as file:
            data = file.readlines()

        for i in range(len(data)):
            data[i] = data[i].replace(old_str, new_str)

        with open(f'{file_name}', 'w') as file:
            file.writelines(data)

    except FileNotFoundError:
        print('An error occurred')


def del_file(file_name):
    try:
        os.remove(f'{file_name}')
    except FileNotFoundError:
        print('An error occurred')


cmd = input()
while not cmd == 'End':
    command, *args = cmd.split('-')
    if command == 'Create':
        create_file(args.pop())
    elif command == 'Add':
        add_to_file(args[0], args[1])
    elif command == 'Replace':
        replace_str_in_file(args[0], args[1], args[2])
    elif command == 'Delete':
        del_file(args.pop())

    cmd = input()
