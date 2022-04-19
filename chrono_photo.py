
'''
4/19/2022

This program will organize all the photos in a folder in chronological order by when they were taken and rename them to their order
'''
import re
import sys
from os import rename
from pathlib import Path
from PIL import Image

path = sys.argv[1]
dates = []

# finding the metadata for when the photos were taken
for child in Path(path).iterdir():
    file = "{}/{}".format(path,child.name)
    with Image.open(file) as image:
        exifdata = image.getexif()

        data = exifdata.get(306)
        dates.append([data,child.name])

dates = sorted(dates)

for i, j in enumerate(dates):
    
    t = re.search(r"\.\w+",j[1])
    ext = t.group()
    #filepath = path +'/'+ j[1]
    new_name = str(i)+ext
    #filepath.rename(path / new_name)
    
    rename(path +'/'+ j[1],path+'/'+ new_name)
    
print("Done")
    
