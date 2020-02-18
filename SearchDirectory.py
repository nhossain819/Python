"""
List All Files in a Directory, Search Directory
The following program lists all files in a folder on the desktop allowing for files to be searched.
"""

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('/Users/Nayeem/Desktop/WORKING'):
        f.append(filenames)

searchlist = []

for i1 in f:
    for i2 in i1:
        if i2 == 'testfile.csv':
            searchlist.append(i2)

print(searchlist)
