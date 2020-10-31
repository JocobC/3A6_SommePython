#!/usr/bin/env python3

"""
Programme pour vérifier océans.txt

Par Jacob Clermont
"""

import colorama
from colorama import Fore, Style
import sys


def main() -> None:
    try:
        with open("océans.txt") as ocean:
            text = ocean.read()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "Le fichier 'océans.txt' n'existe pas.")
        sys.exit(1)

    print(Style.BRIGHT + Fore.CYAN + text)


if __name__ == '__main__':
    main()
