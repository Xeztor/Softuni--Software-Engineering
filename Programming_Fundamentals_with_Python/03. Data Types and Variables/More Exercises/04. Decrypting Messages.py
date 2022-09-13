key = int(input())
lines = int(input())

word = ""

for i in range(lines):
    word += chr(ord(input()) + key)

print(word)
