import re

with open('text.txt', 'r') as file:
    data = file.readlines()

for i in range(len(data)):
    letters = len(re.findall(r'\w', data[i]))
    marks = len(re.findall(r'[!?,.-]', data[i]))
    print(f"Line {i}: {data[i]} ({letters})({marks})")