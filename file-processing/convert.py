from os import path
from PIL import Image
from datetime import datetime

# Libraries
import loglib as log
import filelib as fb
import cli as cli

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


userPath = cli.getPath()
passedArgs = cli.getArgs()

if len(passedArgs) >= 2:
    filePath = f'{userPath}/{passedArgs[0]}'
    saveDir = f'{userPath}/{passedArgs[1]}'

    fb.createPathsIfNotExist(filePath, saveDir)
    log.trace(f'File Path => {filePath}')
    # log.trace(f'Save Path => {saveDir}')

    if path.exists(filePath) and path.exists(saveDir):
        paths = fb.getFiles()
        convert(paths)
    else:
        log.error(f'Failed to find path [{filePath}].')
else:
    log.error(f'Missing arguments, only {len(passedArgs)} supplied.')