path = input().split("\\")

file_name, ext = path[-1].split('.')
print(f'File name: {file_name}\nFile extension: {ext}')
