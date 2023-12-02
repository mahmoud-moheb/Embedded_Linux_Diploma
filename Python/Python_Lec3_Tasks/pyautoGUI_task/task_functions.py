#!/usr/bin/python3
import pyautogui
import os
import time
def open_prog(prog_name):
    pyautogui.hotkey('win')
    time.sleep(0.5)
    pyautogui.typewrite(prog_name)
    pyautogui.hotkey('enter')

def open_extensions():
    with pyautogui.hold('ctrl'):
        with pyautogui.hold('shift'):
            pyautogui.press('x')
    time.sleep(0.5)

def extension_install(extension_name):
    dir_path=os.path.dirname(os.path.realpath(__file__))
    img_path=dir_path+"/SearchExtensions.png"
    locationonscreen=None
    while locationonscreen is None:
        locationonscreen = pyautogui.locateOnScreen(img_path,confidence=0.7)
    pyautogui.moveTo(pyautogui.center(locationonscreen))
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(extension_name, interval=0.05)
    time.sleep(4)
    img_path=dir_path+"/"+extension_name+".png"
    locationonscreen=None
    while locationonscreen is None:
        locationonscreen = pyautogui.locateOnScreen(img_path,confidence=0.7)
    pyautogui.moveTo(pyautogui.center(locationonscreen))
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    img_path=dir_path+"/disable.png"
    locationonscreen=None
    while locationonscreen is None:
        locationonscreen = pyautogui.locateOnScreen(img_path,confidence=0.7)
    if locationonscreen is not None:
        print(extension_name+" was installed before")
    else:
        img_path=dir_path+"/install.png"
        locationonscreen=None
        while locationonscreen is None:
            locationonscreen = pyautogui.locateOnScreen(img_path,confidence=0.7)
        pyautogui.moveTo(pyautogui.center(locationonscreen))
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        print(extension_name+" is installed successfully")

    img_path=dir_path+"/searchbox"+extension_name+".png"
    locationonscreen=None
    while locationonscreen is None:
        locationonscreen = pyautogui.locateOnScreen(img_path,confidence=0.7)
    pyautogui.moveTo(pyautogui.center(locationonscreen))
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    with pyautogui.hold('ctrl'):
        with pyautogui.hold('a'):
            pyautogui.press('delete')
    time.sleep(1)