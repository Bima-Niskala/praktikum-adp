import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls')

def show_icon():
    icon = """
       ____ ____  __  __ 
      / ___|  __||  \/  |
     | |  _| |__ | |\/| |
     | |_| | |__ | |  | |
      \____|____||_|  |_|
        GEM APPLICATION  
    """
    print(colored(icon, 'cyan'))

def loading_screen():
    clear_screen()
    show_icon()
    print(colored("\nMemuat aplikasi, harap tunggu...", 'yellow'))
    
    for i in range(25):
        print(colored("_" * (i + 1) + "-" * (24 - i), 'cyan'), end='\r')
        time.sleep(0.5)
    print(colored("\nAplikasi berhasil dimuat!", 'green'))

loading_screen()