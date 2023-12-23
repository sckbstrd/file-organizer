"""
file_organizer.py

This script organizes files in a directory by creating subdirectories based on file types.
"""

import sys
from os import listdir, makedirs, getcwd, path
from os.path import isfile, join
import shutil

try:
    mypath = sys.argv[1]
except IndexError:
    mypath = getcwd()

print(mypath)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
try:
    onlyfiles.remove(path.basename(__file__))
except ValueError:
    pass
file_types = set() 

for file in onlyfiles:
    extension = file[-file[::-1].find('.')-1:].lower()
    file_types.add(extension)

file_types = list(file_types)

file_types.sort(key=str.lower)

for file in file_types:
    try:
        makedirs(f'{file} files')
    except FileExistsError:
        print('FileExistsError')

for file in onlyfiles:
    extension = file[-file[::-1].find('.')-1:].lower()
    shutil.move(file, f'{extension} files/')

with open("Types of Files in This Directory.txt", 'w', encoding='utf-8') as f:
    f.write(", ".join(file_types))
