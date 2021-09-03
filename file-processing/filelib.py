from pathlib import Path
from os import walk

def getPath(*args):
    str = ''
    for arg in args:
        str += arg
    return str

def createPathsIfNotExist(*args):
    for arg in args:
        createIfNotExists(arg)

def createIfNotExists(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def writeToFile(path, txt = None):
    createIfNotExists(path)
    if txt != None:
        file = open(path, 'w')
        file.write(txt)
        file.close()

def getFiles(pathArgs):
    files = []
    for (path, dirNames, fileNames) in walk(pathArgs):
        files.extend(fileNames)
    return files