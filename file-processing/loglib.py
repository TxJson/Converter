from termcolor import colored
from datetime import datetime
import os

import filelib as fb

logDir = os.getcwd() + '/log/file-processing'

filePath = f'{logDir}/{datetime.now():%Y%m%d-%H%M%S%z}.log'

class headers():
    DEFAULT = ''
    INFO = '[Info]'
    ERROR = '[Error]'
    WARNING = '[Warning]'

def log(msg, hType, color, default = 'Something went wrong'):
    message = msg if msg != None else default
    print(composeMsg(message, color, hType))
    fb.writeToFile(f"{hType} {message}")
    

def composeMsg(msg, color = 'white', hType = headers.DEFAULT):
    return colored(f"{hType} {msg}", color)

def warning(msg = None):
    log(msg, headers.WARNING, 'yellow')

def error(msg = None):
    log(msg, headers.ERROR, 'red')

def info(msg = None):
    log(msg, headers.INFO, 'white')