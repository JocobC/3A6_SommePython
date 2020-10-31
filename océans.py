#!/usr/bin/env python3

"""
Programme pour qui print un fichier texte

Par Jacob Clermont
"""

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("océans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

with open("océans.txt", "a") as f:
    print(23*"=", file=f)
    print("Les cinq océans, par Jacob Clermont", file=f)
