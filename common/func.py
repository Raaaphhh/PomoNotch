from rich.console import Console
from rich.text import Text

console = Console()

def draw_menu():
    console.clear()
    width = console.width

    if width >= 83:
        console.print(Text(f"""\
╔═════PomoNotch v1.0.0═════════════╦═════════════════════════════════════════════╗
║                                  ║                                             ║
║            Welcome !             ║ 1 : Choose a duration below                 ║
║                                  ║ 2 : Start the timer by pressing "enter"     ║
║      A simple way to stay ....   ║ 3 : Focus on your tasks until the break     ║
║           PRODUCTIVE             ║ 4 : You'll be notified when it's break time ║
║                                  ║                                             ║
╚══════════════════════════════════╩═══════════════════════Made with ♥ for fun═══╝"""))

    elif width >= 40:
        console.print(Text(f"""\
╔═════PomoNotch v1.0.0════════╗
║          Welcome !          ║
║   A simple way to stay...   ║
║          PRODUCTIVE         ║
╠═════════════════════════════╣
║ 1 : Choose a duration       ║
║ 2 : Start the timer         ║
║ 3 : Focus on your tasks     ║
║ 4 : Break notification      ║
╚═════════Made with ♥ for fun═╝"""))

    else:
        console.print(Text(f"""\
PomoNotch v1.0.0
  Welcome !
  Stay PRODUCTIVE"""))

if __name__ == "__main__":
    draw_menu()
