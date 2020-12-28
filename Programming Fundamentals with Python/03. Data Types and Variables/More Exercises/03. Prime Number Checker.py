a = int(input())

for divider in range(2, a + 1):
    result = a / divider
    if result.is_integer():
        result = int(result)
        if result != 1:
            print("False")
            break
        else:
            print("True")
