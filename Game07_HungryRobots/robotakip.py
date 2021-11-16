import random, sys, time
from termcolor import colored

BOARD_WITH = 80
BOARD_HEIGHT = 40
GHOST_COUNT = 10
TELEFPORT_COUNT = 2
DEAD_GHOSTS = 2
WALL_COUNT = 100
GHOST = '👻'  # Oyuncuyu kovalayan hayaletler
PLAYER = '🦊'  # Oyuncu
EMPTY_SPACE = ' '
GHOST_HUNTER = '👽'  # Hayaletler çarptığında onları öldüren avcılar
WALL = chr(9617)  # Duvar sembolümüz


def main():
    print(colored('Hayaletten kaç oyununa hoş geldin', 'cyan'))


if __name__ == '__main__':
    main()