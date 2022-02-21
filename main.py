from pyautogui import *
import pyautogui
from os import system
from time import sleep

# El cliente tiene que estar en 1336 x 768 y en español


def click(x,y) -> None:
    pyautogui.moveTo(x,y)
    pyautogui.click()
    

def accept(img_path: str) -> bool:
    pop: bool = False
    print("\n\nIn queue...")
    
    while (not pop):
        img_in_screen = pyautogui.locateOnScreen(img_path,confidence=0.8)
        
        if (img_in_screen != None):
            sleep(7)
            click(img_in_screen.left,img_in_screen.top)
            system('cls')
            pop = True

    return pop


def check_if_cancel(img_path: str) -> bool:
    system('cls')
    print("...")
    sleep(5)
    img = pyautogui.locateOnScreen(img_path,confidence=0.8)
    
    if (img != None):
        return True
    
    return False


def check_if_dodge(img_path: str) -> bool:
    dodged: bool = False
    sec: int = 130

    while (not dodged and sec >= 1):
        system('cls')
        print(f'{sec}')
        print('Waiting for the in-game screen...')
        sleep(1)
        sec -= 1
        in_q = pyautogui.locateOnScreen(img_path,confidence=0.8)
        
        if (in_q != None):
            dodged = True

    return dodged


def main() -> None:
    system('cls')
    
    print("""
             _                
  __ _ _   _| |_ ___          
 / _` | | | | __/ _ \         
| (_| | |_| | || (_) |        
 \__,_|\__,_|\__\___/                   _            
                __ _  ___ ___ ___ _ __ | |_ 
               / _` |/ __/ __/ _ \ '_ \| __|
              | (_| | (_| (_|  __/ |_) | |_ 
               \__,_|\___\___\___| .__/ \__|
                                 |_|             
                                        
                                        by murda""")

    ingame: bool = False

    accept('images/accept_buttom.png')
    canceled: bool = check_if_cancel('images/in_q.png')
    
    while (not ingame):   
            
        if (canceled):
            accept('images/accept_buttom.png')
            canceled = check_if_cancel('images/in_q.png')
        
        else:
            dodged = check_if_dodge('images/in_q.png')
            
            if (dodged):
                accept('images/accept_buttom.png')
                canceled = check_if_cancel('images/in_q.png')     
            else:
                ingame = True
       
main()            