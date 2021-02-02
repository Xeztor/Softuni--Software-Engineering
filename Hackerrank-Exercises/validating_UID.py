import re

pattern = r'(?!^.*([0-9A-Za-z]).*\1)(?=(?:^.*([A-Z].*[A-Z])))(?=(?:\b([A-Za-z0-9]{10}\b)))(?=(?:^(.*(\d)){3}))'

for _ in range(int(input())):
    uid = input()

    if re.search(pattern, uid):
        print('Valid')
    else:
        print('Invalid')