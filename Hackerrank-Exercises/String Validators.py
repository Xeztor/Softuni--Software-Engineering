string = input()

alnum = [i for i in string if i.isalnum()]
alpha = [i for i in string if i.isalpha()]
num = [i for i in string if i.isdigit()]
lower = [i for i in string if i.islower()]
upper = [i for i in string if i.isupper()]

if alnum:
    print(True)
else:
    print(False)
if alpha:
    print(True)
else:
    print(False)
if num:
    print(True)
else:
    print(False)
if lower:
    print(True)
else:
    print(False)
if upper:
    print(True)
else:
    print(False)
