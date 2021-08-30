import os
import sys
from os import walk
from os import path
from PIL import Image
from datetime import datetime

# Libraries
import loglib as log
import filelib as fb


passedArgs = sys.argv[slice(1, len(sys.argv))]

filesPath = passedArgs[0] or os.getcwd() + '/img'
saveDir = passedArgs[1] or os.getcwd() + '/converted-pdfs'

fb.createIfNotExists(filesPath)
fb.createIfNotExists(saveDir)
log.trace(f'File Path => {filesPath}')
log.trace(f'Save Path => {saveDir}')

def getFiles():
    files = []
    for (path, dirNames, fileNames) in walk(filesPath):
        files.extend(fileNames)
        break
    return files

def convert(files):
    try:
        fb.createIfNotExists(saveDir)
        
        imgs = []
        for file in files:
            image = Image.open(rf'{filesPath}/{file}')
            ci = image.convert('RGB')
            imgs.append(ci)

        if len(imgs) > 0:
            img = imgs[0]
            imgs.pop(0)
            img.save(rf'{saveDir}/{datetime.now():%Y%m%d-%H%M%S%z}.pdf', save_all=True, append_images=imgs)
    except AssertionError as error:
        log.error('Conversion failed')
        pass

if path.exists(filesPath):
    paths = getFiles()
    convert(paths)
else:
    log.error('Failed to find path ' + filesPath)