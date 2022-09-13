substr = input().split(", ")
str_list = input().split(", ")

matches = []

for i in range(len(substr)):
    for j in range(len(str_list)):
        if substr[i] in str_list[j] and substr[i] not in matches:
            matches.append(substr[i])

print(matches)
