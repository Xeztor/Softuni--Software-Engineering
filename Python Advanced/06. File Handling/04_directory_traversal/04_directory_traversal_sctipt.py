from os import listdir
from os.path import isfile, join
from collections import defaultdict
from pathlib import Path


def get_only_files(directory):
    only_files = [f for f in listdir(f'{directory}') if isfile(join('.', f))]
    return only_files


def get_extensions_dict(files):
    files_dict = defaultdict(list)
    for file in files:
        name, ext = file.split('.')
        files_dict['.' + ext].append(file)

    return files_dict


def verbose(files_dict):
    lines = []
    for ext, names in sorted(files_dict.items(), key=lambda x: x[0]):
        lines.append(ext + '\n')
        for file_name in sorted(names):
            lines.append(f'- - - {file_name}\n')

    home = str(Path.home())
    with open(f"{home}\\Desktop\\report.txt", 'w') as file:
        file.writelines(lines)


directory = input()
dir_files = get_only_files(directory)
files_data = get_extensions_dict(dir_files)
verbose(files_data)
