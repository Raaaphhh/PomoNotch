import subprocess
import time
import os
import sys
import cutie
from common.func import draw_menu

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# GLOBAL COLOR VARIABLES
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
WHITE = "\033[97m"
RESET = "\033[0m"

def timerGo(timeFocus, timeBreak):
    timeFocusInSec = timeFocus * 60
    timeBreakInSec = timeBreak * 60
    paused = False

    while (timeFocusInSec > 0):
        if not paused :
            minutes, seconds = divmod(timeFocusInSec, 60)
            width = os.get_terminal_size().columns
            if width >= 40:
                msg = f"\rOnly {GREEN}{minutes}min {seconds}s{RESET} left before a {RED}{timeBreak}min{RESET} break"
            else:
                msg = f"\r{GREEN}{minutes}:{seconds:02d}{RESET}"
            print(msg, end="", flush=True)
            timeFocusInSec -= 1
            time.sleep(1)

        if(timeFocusInSec == 0):
            notch_dir = os.path.join(BASE_DIR, "notch")
            sound_proc = subprocess.Popen(["afplay", os.path.join(BASE_DIR, "sounds/sound_start_break.mp3")])
            notch_proc = subprocess.Popen(["./notch_binary", str(timeBreakInSec)], cwd=notch_dir)

            while(timeBreakInSec > 0):
                minutes, seconds = divmod(timeBreakInSec, 60)
                print(f"\rEnjoy your {timeBreak}min break! Only {GREEN}{minutes}min {seconds}s{RESET} left.", end="")
                timeBreakInSec -= 1
                time.sleep(1)
            
            sound_eb = subprocess.Popen(["afplay", os.path.join(BASE_DIR, "sounds/sound_end_break.mp3")])
            notch_proc.wait()
            sound_eb.wait()
    
    # Rajouter une animation de supression du texte de la line de facons linéaire
    return timerGo(timeFocus, timeBreak)

def menu():
    draw_menu()
    choices = [
        "Select your Pomodoro session:",
        "25min focus, 5min rest",
        "45min focus, 15min rest",
        "Custom duration",
        "Leave PomoNotch"
    ]
    captions = [0]
    choice = choices[cutie.select(choices, caption_indices=captions, selected_index=1)]
    if(choice == choices[1]):
        print("\033[5A\033[J", end="", flush=True)
        timerGo(25, 5)
    elif(choice == choices[2]):
        print("\033[5A\033[J", end="", flush=True)
        timerGo(45, 15)
    elif(choice == choices[3]): 
        timeFocusCustom = cutie.get_number("Enter the custom focus duration (in minutes):", min_value=1, allow_float=False)
        timeBreakCustom = cutie.get_number("Enter the custom break duration (in minutes):", min_value=1, allow_float=False)
        print("\033[7A\033[J", end="", flush=True)
        print(f"Every {timeFocusCustom}min you will have an {timeBreakCustom}min break")
        timerGo(timeFocusCustom, timeBreakCustom)
    elif(choice == choices[4]):
        print("\nEnd of work time, Good Bye !!!!")
        print("")
        return
    return

menu()