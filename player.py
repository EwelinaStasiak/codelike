from game_map import *
from inventory import *

class PlayerType:
    A = 0
    B = 1


class Player:
    def __init__(self, health, strength, force):
        self.health = health
        self.strength = strength
        self.force = force



def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def moving_player(game_map, player_location):
    player_x = player_location[0]
    player_y = player_location[1]
    print('Press W(up), S(down), A(left), D(right)')
    while True:
        input_moving = getch().upper()
        if input_moving == 'W':
            if game_map[player_x][player_y - 1].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_y -= 1
        elif input_moving == 'S':
            if game_map[player_x][player_y + 1].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_y += 1
        elif input_moving == 'A':
            if game_map[player_x - 1][player_y].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_x -= 1
        elif input_moving == 'D':
            if game_map[player_x + 1][player_y].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_x += 1
        game_map[player_x][player_y].tile = Tile.PLAYER
        print_map(game_map)
