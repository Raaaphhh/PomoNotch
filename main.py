import subprocess
import time
import sys
import os
import cutie
import select

# GLOBAL COLOR VARIABLES
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def timerGo(timeFocus, timeBreak):
    timeFocusInSec = timeFocus * 60
    timeBreakInSec = timeBreak * 60
    paused = False
    exit = False

    while (timeFocusInSec > 0):
        if not paused : 
            minutes, seconds = divmod(timeFocusInSec, 60)
            print(f"\rOnly {GREEN}{minutes}min {seconds}s{RESET} left before a {RED}{timeBreak}min{RESET} break", end="")
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
            # APPEL POUR AFFICHER NOTCH ici 
            # Notification ci dessous : 
            subprocess.run(["osascript", "-e", 'display notification "Pause !" with title "PomoNotch"'])
            os.system('clear')
            while(timeBreakInSec > 0):
                minutes, seconds = divmod(timeBreakInSec, 60)
                print(f"\rEnjoy your {timeBreak}min break! Only {minutes}min {seconds}s left.", end="")
                timeBreakInSec -= 1
                time.sleep(1)
    
    os.system('clear')
    print("Here we go for an other tour !")
    return timerGo(timeFocus, timeBreak)


def menu():
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
        timerGo(25, 5)
    elif(choice == choices[2]):
        timerGo(45, 15)
    elif(choice == choices[3]): 
        timeFocusCustom = cutie.get_number("Enter the custom focus duration (in minutes):", min_value=1, allow_float=False)
        timeBreakCustom = cutie.get_number("Enter the custom break duration (in minutes):", min_value=1, allow_float=False)
        os.system('clear')
        print(f"So every {timeFocusCustom}min you will have an {timeBreakCustom}min break")
        timerGo(timeFocusCustom, timeBreakCustom)
    elif(choice == choices[4]):
        print("\nEnd of work time, Good Bye !!!!")
        print("")
        return

    return

menu()