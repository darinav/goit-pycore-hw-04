from pathlib import Path
from colorama import Fore, Style
import sys

def print_tree(path: Path, prefix: str = ""):
    entries = list(path.iterdir())
    entries.sort()
    total = len(entries)

    for index, entry in enumerate(entries):
        is_last = index == total - 1
        branch = "└── " if is_last else "├── "

        if entry.is_dir():
            color = Fore.BLUE
        elif entry.suffix == ".py":
            color = Fore.LIGHTYELLOW_EX
        elif entry.suffix == ".txt":
            color = Fore.MAGENTA
        else:
            color = Fore.LIGHTCYAN_EX

        print(f"{prefix}{branch}{color}{entry.name}{Style.RESET_ALL}")

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(entry, prefix + extension)

def visualise_structure(path_str: str):
    path = Path(path_str)
    if not path.exists() or not path.is_dir():
        print("Шлях не існує або не є директорією.")
        return
    print_tree(path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії як аргумент.")
    else:
        visualise_structure(sys.argv[1])
