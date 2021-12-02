import random, sys
from termcolor import COLORS, colored

HANGMAN_PICS = [
    r"""
 +--+
 |  |
    |
    |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""", r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
]


def main():
    print(
        colored(
            """        
        Adam Asmaca oyununa hoş geldin !!!

        Hazır olduğunda bir tuşa bas ;)
    """, "cyan"))
    input(colored('..:', 'cyan'))


if __name__ == '__main__':
    # Normalde program çalışırken Ctrl+C'ye basıldığında uygulama interrupt olur.
    # Bunu KeyboardInterrupt'ta yakalayıp sys.exit() ile düzgün bir çıkış sağlıyoruz.
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()