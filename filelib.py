from pathlib import Path

def getPath(*args):
    str = ''
    for arg in args:
        str += arg
    return str


def createIfNotExists(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def writeToFile(path, txt):
    createIfNotExists(path)
    file = open(path, 'w')
    file.write(txt)
    file.close()