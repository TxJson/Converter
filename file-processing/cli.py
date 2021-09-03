import sys

def getPath():
    return sys.path[0]

def getArgs():
    return sys.argv[slice(1, len(sys.argv))]