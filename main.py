from time import sleep
import pyautogui
from keyboard import press
from tqdm import tqdm
import time
import sys
from colorama import Fore, Back, Style
import webbrowser
import reloadex

url = "https://github.com/dannybanno"

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.000000001)

delay_print(Fore.RED + '''

 █████╗ ██╗   ██╗████████╗ ██████╗       ███████╗██████╗  █████╗ ███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗      ██╔════╝██╔══██╗██╔══██╗████╗ ████║
███████║██║   ██║   ██║   ██║   ██║█████╗███████╗██████╔╝███████║██╔████╔██║
██╔══██║██║   ██║   ██║   ██║   ██║╚════╝╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝      ███████║██║     ██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝       ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                                            
Made by dannybanno#1848

''')

Word = input("Enter the Word You Want To Spam: ")

AmmountTime = input("Enter The Ammount Of Times You Want To Spam: ")

print("You Have 5 Seconds To Click The Message Bar")

for i in tqdm(range(10)):
    sleep(0.5)
print("Spam Incoming!!!")
for i in range(0, int(AmmountTime)):
    pyautogui.typewrite(Word)
    press('enter')

for i in range (1):
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)


    delay_print(Fore.GREEN + '''Thank you for downloading this file
    
    Please also checkout my github https://github.com/dannybanno <3
    ''')
    delay_print(Fore.YELLOW + "[1] - exit: ")
    exnd = input()
    if exnd == "1":
        print("bye!")
        webbrowser.open_new(url)
        exit()

