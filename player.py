from game_map import *
from inventory import *


class Player:
    ZDZISLAW = 'Zdzisław'
    HENRYK = 'Henryk'

    def __init__(self, x, y, type_hero):
        self.type_hero = type_hero
        self.x = x
        self.y = y
        self.inventory = []

        if type_hero == Player.ZDZISLAW:
            self.health = 50
            self.damage = 5
            self.defense = 3
            self.to_hit = 4
        elif type_hero == Player.HENRYK:
            self.health = 55
            self.damage = 4
            self.defense = 2
            self.to_hit = 5


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


def determine_action_type(player, new_x, new_y, game_map):
    if game_map[new_x][new_y].tile == Cell.EMPTY:
        game_map[player.x][player.y].tile = Cell.EMPTY
        player.x = new_x
        player.y = new_y
        game_map[player.x][player.y].tile = Cell.PLAYER
        return True


def action_of_player(game_map, player):
    player_finished_turn = False
    input_moving = getch().upper()
    if input_moving == 'W':
        player_finished_turn = determine_action_type(player, player.x, player.y - 1, game_map)
    elif input_moving == 'S':
        player_finished_turn = determine_action_type(player, player.x, player.y + 1, game_map)
    elif input_moving == 'A':
        player_finished_turn = determine_action_type(player, player.x - 1, player.y, game_map)
    elif input_moving == 'D':
        player_finished_turn = determine_action_type(player, player.x + 1, player.y, game_map)
    elif input_moving == 'P':
        player_finished_turn = True
    elif input_moving == 'I':
        print_inventory(player.inventory)

    game_map[player.x][player.y].tile = Cell.PLAYER
    return player_finished_turn
