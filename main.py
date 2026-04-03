import subprocess
import time
import sys
import os
import signal
import cutie
import select
from common.func import draw_menu, on_resize

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
    exit = False

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

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            user_input = sys.stdin.read(1).strip()
            if user_input.lower() == "p":
                paused = not paused
                if paused:
                    print("\nTimer paused. Press 'p' to resume.")
                else:
                    print("\nTimer resumed.")
            elif user_input.lower() == "e":
                exit = not exit
                if exit:
                    print("\nEnd of work time, Good Bye !!!!")
                    return

        if(timeFocusInSec == 0):
            # Essayer de faire une notif sonore
            # subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
            # APPEL AFFICHAGE NOTCH : 
            subprocess.run(["swiftc", "main.swift", "RoundedView.swift", "NotchAnimation.swift", "-o", "notch_binary", "-framework", "Cocoa"], cwd="notch")
            notch_proc = subprocess.Popen(["./notch_binary", str(timeBreakInSec)], cwd="notch")

            while(timeBreakInSec > 0):
                # Ajouter logique de pause
                minutes, seconds = divmod(timeBreakInSec, 60)
                print(f"\rEnjoy your {timeBreak}min break! Only {GREEN}{minutes}min {seconds}s{RESET} left.", end="")
                timeBreakInSec -= 1
                time.sleep(1)
            notch_proc.wait()
    
    # Rajouter une animation de supression du texte de la line de facons linéaire
    return timerGo(timeFocus, timeBreak)

def menu():
    signal.signal(signal.SIGWINCH, on_resize)
    draw_menu()
    signal.signal(signal.SIGWINCH, signal.SIG_IGN)
    choices = [
        "Select your Pomodoro session:",
        "25min focus, 5min rest",
        "45min focus, 15min rest",
        "Custom duration",
        "Leave PomoNotch"
    ]
    captions = [0]
    choice = choices[cutie.select(choices, caption_indices=captions, selected_index=1)]
    signal.signal(signal.SIGWINCH, on_resize)
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