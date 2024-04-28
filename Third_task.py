import sys
import os
from pathlib import Path
from colorama import Fore, Style, init

# ініціалізація colorama для використання в Windows
init()

# Визначення функції для рекурсивного обходу директорії
def list_directory_structure(path: Path, indent: int = 0):
    if not path.exists():
        print(Fore.RED + f"Path '{path}' does not exist." + Style.RESET_ALL)
        return

    if not path.is_dir():
        print(Fore.RED + f"Path '{path}' is not a directory." + Style.RESET_ALL)
        return

    # Відступ для ієрархічної структури
    indent_str = ' ' * (indent * 2)

    # Перевірка піддиректорій та файлів
    for item in sorted(path.iterdir(), key=lambda x: (x.is_dir(), x.name.lower())):
        if item.is_dir():
            # Директорії виділяються синім кольором
            print(f"{indent_str}{Fore.BLUE}[DIR] {item.name}{Style.RESET_ALL}")
            # Рекурсивний обхід піддиректорії
            list_directory_structure(item, indent + 1)
        else:
            # Файли виділяються зеленим кольором
            print(f"{indent_str}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

# Перевірка аргументу командного рядка
if len(sys.argv) != 2:
    print(Fore.RED + "Usage: python script.py <path-to-directory>" + Style.RESET_ALL)
    sys.exit(1)

directory_path = Path(sys.argv[1])

# Вивід структури директорії
list_directory_structure(directory_path)
