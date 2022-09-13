first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text = [matrix[j][i] for i in range(m) for j in range(len(matrix))]

decoded = []
crnt_i = 0
flag = False

for _ in range(len(text)):
    while text and text[crnt_i].isalnum():
        while text and text[crnt_i].isalnum():
            decoded.append(text[crnt_i])
            crnt_i = 0
            text.pop(0)

        word = []
        while crnt_i < len(text) and not text[crnt_i].isalnum():
            word.append(text[crnt_i])
            crnt_i += 1

        while len(word) == len(text):
            flag = False
            break
        else:
            flag = True

        while not flag:
            decoded.extend(word)
            text.clear()
            break
        else:
            del text[:len(word)]
            word.clear()
            decoded.append(' ')
            crnt_i = 0
    while text:
        decoded.append(text[crnt_i])
        text.pop(0)
        crnt_i = 0
        break

print("".join(decoded))