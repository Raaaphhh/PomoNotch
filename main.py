import time
import sys
import os
import curses

# print("Votre durée de travail(min) :")
# timerInMin = int(input())
# timerInSec = timerInMin * 60

def menu(stdscr):
    # Désactiver le curseur
    curses.curs_set(0)

    # Liste des options
    options = ["Option 1", "Option 2", "Option 3", "Quitter"]
    current_selection = 0

    while True:
        stdscr.clear()

        # Afficher les options
        for i, option in enumerate(options):
            if i == current_selection:
                stdscr.addstr(i, 0, f"> {option}", curses.A_REVERSE)  # Option sélectionnée
            else:
                stdscr.addstr(i, 0, f"  {option}")

        stdscr.refresh()

        # Récupérer l'entrée utilisateur
        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key == ord("\n"):  # Touche Entrée
            if options[current_selection] == "Quitter":
                # appeler fonction de fermeture programe
                break
            elif options[current_selection] == "25min work, 5min break":
                printTimer(25, 5)
            elif options[current_selection] == "45min work, 10min break":
                printTimer(45, 15)
            elif options[current_selection] == "Personnalisé":
                print("Give a Minute of work : ")
                timeWork = int(input())
                print("Give a Minute of break : ")
                timeBreak = int(input())
                printTimer(timeWork, timeBreak)
            stdscr.addstr(len(options) + 1, 0, f"Vous avez sélectionné: {options[current_selection]}")
            stdscr.refresh()
            stdscr.getch()  # Pause pour afficher le message


def printTimer(timerInMin, timerBreak):
    timerInSec = timerInMin * 60
    while(timerInSec > 0):
        minutes = timerInSec // 60
        seconds = timerInSec % 60
        os.system('clear')
        sys.stdout.write(f"\rEncore : {minutes:02d}:{seconds:02d}")
        sys.stdout.flush()
        time.sleep(1)
        timerInSec -= 1 
    print("\rTemps écoulé !            ")
    return

curses.wrapper(menu)
# printTimer(timerInSec)