import os
import sys
from random import choice
from keyboard import is_pressed
from time import sleep

def Image_Caller():   
    path_loc = f"{sys.path[0]}\Photos"

    photo_names = os.listdir(path_loc)
    photo_chosen = choice(photo_names)

    os.system(f"\"{path_loc}\\{photo_chosen}\"")
    
    while True:
        if is_pressed("f"):
            #Kill process uisng pid/image name/process name
            os.system("taskkill /im PhotosApp.exe /f")

            photo_chosen = choice(photo_names)
            os.system(f"\"{path_loc}\\{photo_chosen}\"")
        sleep(0.2)

if __name__ == "__main__":
    Image_Caller()
    
    
