import keyboard
import mouse
import time
from colorama import Fore

reaction = True

def sgputar():
    mouse.click('left')
    keyboard.press_and_release('3')
    keyboard.press_and_release('1')

print(Fore.GREEN + 'Macro SG Is Running....')

def on_key_event(event):
    if event.name == 'alt+1':
        print(Fore.RED + 'Macro SG Is Stopp....')
        global reaction
        reaction = False

keyboard.hook(on_key_event)

while reaction:
    if (mouse.is_pressed('right')):
        sgputar()
        time.sleep(0.1)