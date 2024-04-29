'''
heic2jpg.py

Convert HEIC images (iPhone image format) to jpg.
Works on either a single file, or a file folder.
'''

from PIL import Image
from pillow_heif import register_heif_opener
import sys
import os

def convertImage(imagepath: str):
    '''
    Convert single .HEIC image to jpg.
    '''

    if not os.path.splitext(imagepath)[1][1:].upper() == 'HEIC':
        print(f'{imagepath} does not have the HEIC extension')
        return

    try:
        image = Image.open(imagepath)
    except Exception as e:
        print(f'Whoops: {e}')
        return

    rgb = image.convert("RGB")
    image.close()
    rgb.save(f'{imagepath}.jpg')

def convertDirectory(path: str):
    '''
    Loop through files in a folder, looking for HEIC and convert
    to jpg.
    '''
    for files in os.listdir(path):
        if os.path.splitext(files)[1][1:].upper() == 'HEIC':
            convertImage(files)

def main():
    args = sys.argv

    if len(args) < 2:
        print("Did you forget something...?")
        print("heic2jpg <file name | folder name>")
        sys.exit()

    register_heif_opener()

    # This is just a single file
    if os.path.isfile(args[1]):
        convertImage(args[1])

    # Loop through the folder
    elif os.path.isdir(args[1]):
        convertDirectory(args[1])

    else:
        print(f'{args[1]} is not a file nor file folder.')
        return
    

if __name__ == "__main__":
    main()