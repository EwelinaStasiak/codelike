from game_map import *
from inventory import *


class PlayerType:
    A = 0
    B = 1


class Player:
    def __init__(self, x, y, health, strength, force, to_hit, defense):
        self.x = x
        self.y = y
        self.health = health
        self.strength = strength
        self.force = force
        self.to_hit = to_hit
        self.defense = defense
        self.inventory = []


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


def action_of_player(game_map, player):
    print('Press W(up), S(down), A(left), D(right)')
    player_finished_turn = False
    input_moving = getch().upper()
    if input_moving == 'W':
        if game_map[player.x][player.y - 1].tile == Tile.EMPTY:
            game_map[player.x][player.y].tile = Tile.EMPTY
            player.y -= 1
            player_finished_turn = True
    elif input_moving == 'S':
        if game_map[player.x][player.y + 1].tile == Tile.EMPTY:
            game_map[player.x][player.y].tile = Tile.EMPTY
            player.y += 1
            player_finished_turn = True
    elif input_moving == 'A':
        if game_map[player.x - 1][player.y].tile == Tile.EMPTY:
            game_map[player.x][player.y].tile = Tile.EMPTY
            player.x -= 1
            player_finished_turn = True
    elif input_moving == 'D':
        if game_map[player.x + 1][player.y].tile == Tile.EMPTY:
            game_map[player.x][player.y].tile = Tile.EMPTY
            player.x += 1
            player_finished_turn = True
    elif input_moving == 'P':
        player_finished_turn = True
    elif input_moving == 'I':
        print_inventory(player.inventory)
        # while True:
        #     use_item(inventory)

    game_map[player.x][player.y].tile = Tile.PLAYER
    return player_finished_turn
