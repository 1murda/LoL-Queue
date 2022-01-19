from pyautogui import *
import pyautogui


def check() -> bool:
    button_pos = pyautogui.locateOnScreen('accept_buttom.png', confidence=0.8)

    if(button_pos != None):
        pyautogui.moveTo(button_pos.left, button_pos.top)
        pyautogui.click()

        return True
    
    return False

def main() -> None:

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
                                        nashe""")
    
    print('\n\nIn queue...')
    pop: bool = False
    
    while(not pop):
        pop = check()   

main()            