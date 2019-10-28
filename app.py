import os
from random import randint


def error(msg):
    print(msg)
    exit(1)

def moveFile(filename, destinationPath):
    # pass
    oldPath = os.getcwd().replace('\\', '/') + '/' + fileName
    newPath = destinationPath + '/' + fileName

    while(True):
        try:
            os.rename(oldPath, newPath)
        except WindowsError:
            newPath = destinationPath + '/' + str(randint(0, 9999999)) + fileName
        else:
            break            


    print(fileName, " moved successfully!")


allFiles = os.walk(os.getcwd()).next()[2]



for file in allFiles:
    try:
        fileName, fileExt = file.split('.')
    except ValueError:
        print("Couldn't move "+ file)
        continue
    fileName = fileName + '.' +fileExt

    if fileExt.lower() == 'txt':
        # put the file in text folder
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/text')
        
    elif fileExt.lower() in ['jpg', 'jpeg', 'jpe', 'jfif', 'png', 'bmp', 'gif']:
        # put the file in image folder
        # pass
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/images')

    elif fileExt.lower() in ['mp4', 'avi', 'mov', 'wmv']:
        # put the file in video folder
        # pass
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/videos')

    elif fileExt.lower() in ['pdf']:
        # put the file in the eBooks folder
        # pass
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/pdfs')

    elif fileExt.lower() in  ['zip']:
        # pass
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/zipped')

    elif fileExt.lower() in  ['mp3']:
        # pass
        moveFile(fileName, 'C:/Users/Windows/Desktop/temp/songs')

    else:
        print((fileName+'.'+fileExt), ": File format not supported!")
