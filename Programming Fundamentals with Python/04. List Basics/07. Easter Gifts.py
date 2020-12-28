gifts = input()

list_gifts = gifts.split()

command = input()
while not command == "No Money":
    words = command.split()
    if words[0] == "OutOfStock":
        for i in range(len(list_gifts)):
            if list_gifts[i] == words[1]:
                list_gifts[i] = "None"
    elif words[0] == "Required":
        if 0 < int(words[2]) < len(list_gifts) - 1:
            list_gifts[int(words[2])] = words[1]
    elif words[0] == "JustInCase":
        list_gifts[-1] = words[1]
    command = input()

print_list = []
for i in list_gifts:
    if not i == "None":
        print_list.append(i)

print(" ".join(print_list))
