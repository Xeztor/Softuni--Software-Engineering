def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):

        if len(string) < len(sub_string):
            break

        if string[-len(sub_string):] == sub_string:
            count += 1

        string = list(string)
        string.pop()
        string = ''.join(string)

    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)