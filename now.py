#!/usr/bin/env python3

"""
Programme qui affiche des dates

Par Jacob Clermont
"""
import datetime


def main() -> None:
    """Fonction principale"""
    maintenant = datetime.datetime.today()
    noel = datetime.date(2020, 12, 25)
    avantnoel = datetime.date(2020, 12, 25) - maintenant.date()
    print(f"maintenant: {maintenant}")
    print(f"aujourd'hui: {maintenant.date()}")
    print(f"demain: {maintenant.date() + datetime.timedelta(days=1)}")
    print(f"avant-hier: {maintenant.date() + datetime.timedelta(days=-2)}")
    print(f"noel: {noel}")
    print(f"noel dans: {avantnoel.days} jours")


if __name__ == '__main__':
    main()
