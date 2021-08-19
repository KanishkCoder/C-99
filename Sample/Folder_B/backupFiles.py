import os
import shutil

source=input('Enter source folder: ')
destination=input('Enter destination folder: ')
source=source+'/'
destination=destination+'/'

list=os.listdir(source)
for file in list:
    shutil.copy((source+file),destination)