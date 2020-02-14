import pathlib
import os
import re

filename = 'filetypes.txt'
os.chdir(pathlib.Path(__file__).parent.absolute())

pattern = re.compile("\.[a-z0-9]+")


def Directory(value):
    # Decides which directory the files need to be put into
    for category, suffixes in subdirs.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'misc'


def organizeDirectory():
    for item in os.scandir():
        # If directory exists
        if item.is_dir():
            continue
        file_path = pathlib.Path(item)
        file_type = file_path.suffix.lower()
        directory = Directory(file_type)
        directoryPath = pathlib.Path(directory)

        # If directory doesn't exist
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        file_path.rename(directoryPath.joinpath(file_path))


def parse_text_file(fname):
    for i, line in enumerate(open(fname, 'r')):
        if i == 0:
            documents = [match.group()
                         for match in re.finditer(pattern, line)]
        elif i == 1:
            compressed = [match.group()
                          for match in re.finditer(pattern, line)]
        elif i == 2:
            audio = [match.group()
                     for match in re.finditer(pattern, line)]
        elif i == 3:
            videos = [match.group()
                      for match in re.finditer(pattern, line)]
        elif i == 4:
            images = [match.group()
                      for match in re.finditer(pattern, line)]
        elif i == 5:
            disc = [match.group()
                    for match in re.finditer(pattern, line)]
        elif i == 6:
            database = [match.group()
                        for match in re.finditer(pattern, line)]
        elif i == 7:
            executable = [match.group()
                          for match in re.finditer(pattern, line)]
        elif i == 8:
            presentation = [match.group()
                            for match in re.finditer(pattern, line)]
        elif i == 9:
            spreadsheet = [match.group()
                           for match in re.finditer(pattern, line)]

    return {'documents': documents, 'compressed': compressed, 'audio': audio,
            'videos': videos, 'images': images, 'disc': disc, 'database': database, 'executable': executable, 'presentation': presentation, 'spreadsheet': spreadsheet}


subdirs = parse_text_file(filename)
organizeDirectory()
