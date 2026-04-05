from rich.console import Console
from rich.text import Text

# GLOBAL COLOR VARIABLES
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"
GOLD = "\033[33m"

console = Console()

def draw_menu():
    console.clear()
    width = console.width

    if width >= 83:
        console.print(Text(f"""{GOLD}
╭─────{RESET}{BOLD}PomoNotch v1.0.0{RESET}{GOLD}─────────────┬─────────────────────────────────────────────╮
│                                  │                                             │
│             {RESET}{BOLD}Welcome !{RESET}{GOLD}            │ {RESET}{BOLD}1{RESET} : Choose a duration below                 {GOLD}│
│                                  │ {RESET}{BOLD}2{RESET} : Start the timer by pressing "enter"     {GOLD}│
│      A simple way to stay ....   │ {RESET}{BOLD}3{RESET} : Focus on your tasks until the break     {GOLD}│
│           {RESET}{BOLD}PRODUCTIVE{RESET}{GOLD}             │ {RESET}{BOLD}4{RESET} : You'll be notified when it's break time {GOLD}│
│                                  │                                             │
╰──────────────────────────────────┴───────────────────────{RESET}Made with ♥ for fun{GOLD}───╯{RESET}"""))

    elif width >= 40:
        console.print(Text(f"""{GOLD}
╭─────{RESET}{BOLD}PomoNotch v1.0.0{RESET}{GOLD}════════╮
│          {RESET}{BOLD}Welcome !{RESET}{GOLD}          │
│   A simple way to stay...   │
│        {RESET}{BOLD}PRODUCTIVE{RESET}{GOLD}           │
├─────────────────────────────┤
│ {RESET}{BOLD}1{RESET} : Choose a duration       {GOLD}│
│ {RESET}{BOLD}2{RESET} : Start the timer         {GOLD}│
│ {RESET}{BOLD}3{RESET} : Focus on your tasks     {GOLD}│
│ {RESET}{BOLD}4{RESET} : Break notification      {GOLD}│
╰─────────{RESET}Made with ♥ for fun{GOLD}─╯{RESET}"""))

    else:
        console.print(Text(f"""{GOLD}{BOLD}PomoNotch v1.0.0{RESET}
  {BOLD}Welcome !{RESET}
  Stay {GOLD}{BOLD}PRODUCTIVE{RESET}"""))

if __name__ == "__main__":
    draw_menu()
