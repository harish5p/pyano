from pynput import keyboard
import os
import winsound

path = 'wav/'
files = os.listdir(path)

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def on_press(key): 
    try:
        if key.char in keys:
            get_index = keys.index(key.char)
            winsound.PlaySound(f"{path}{files[get_index]}", winsound.SND_ASYNC)        
    except AttributeError:
        print('special key pressed: f"{key}") 

def on_release(key):    
    print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

