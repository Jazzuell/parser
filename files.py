from os import listdir,walk
from os.path import isfile, join
mypath="c://pracovnaverzia/"


def GetFiles(path,filetypes):
    f = []
    filetypes=[".cs",".CS"]
    for (dirpath, dirname, filenames) in walk(path):
        for file in filenames:
            for type in filetypes:
                if (file.endswith(type)):
                    f.append((dirpath + '/' +file))
    return f