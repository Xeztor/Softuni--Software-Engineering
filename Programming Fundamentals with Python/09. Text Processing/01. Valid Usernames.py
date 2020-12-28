usernames = input().split(', ')

valid_users = []

for i in usernames:
    valid = True
    if 3 < len(i) < 16:
        for char in i:
            if ord(char) not in range(65, 91) and \
                    ord(char) not in range(97, 123) and \
                    not char == "_" and \
                    not char == "-":
                valid = False
                break
    else:
        valid = False
    if valid:
        valid_users.append(i)

print('\n'.join(valid_users))
