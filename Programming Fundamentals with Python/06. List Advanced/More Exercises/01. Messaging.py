nums = input().split()
message = list(input())

indexes = []
for i in nums:
    crnt_index = 0
    for j in i:
        crnt_index += int(j)
    indexes.append(crnt_index)

hidden_msg = ""
for i in indexes:
    if (len(message) - 1) - i >= 0:
        hidden_msg += message.pop(i)
    else:
        i = abs(len(message) - i)
        hidden_msg += message.pop(i)

print(hidden_msg)
