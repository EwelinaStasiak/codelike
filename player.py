from fight import test_for_hit, deal_damage
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

    def attack(self, monsters, monster):
        if test_for_hit(self.to_hit, monster.to_hit):
            dealt_damage = deal_damage(self.damage, monster.defense)
            print('You attacked {} with {}. You dealt {} damage.'.format(monster.monster_type, 'Chair', dealt_damage))
            monster.health -= dealt_damage
            if monster.health <= 0:
                # kill
                pass
        else:
            print('You missed {}.'.format(monster.monster_type))


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


def search_for_monster(monsters, new_x, new_y):
    for monster in monsters:
        if monster.x == new_x and monster.y == new_y:
            return monster


def determine_action_type(player, new_x, new_y, game_map, monsters):
    if game_map[new_x][new_y].tile == Cell.EMPTY:
        game_map[player.x][player.y].tile = Cell.EMPTY
        player.x = new_x
        player.y = new_y
        game_map[player.x][player.y].tile = Cell.PLAYER
        return True
    if game_map[new_x][new_y].tile == Cell.RAGING_NERD or game_map[new_x][new_y].tile == Cell.SYSOP:
        monster = search_for_monster(monsters, new_x, new_y)
        player.attack(monsters, monster)
        return True


def action_of_player(game_map, player, monsters):
    player_finished_turn = False
    input_moving = getch().upper()
    if input_moving == 'W':
        player_finished_turn = determine_action_type(player, player.x, player.y - 1, game_map, monsters)
    elif input_moving == 'S':
        player_finished_turn = determine_action_type(player, player.x, player.y + 1, game_map, monsters)
    elif input_moving == 'A':
        player_finished_turn = determine_action_type(player, player.x - 1, player.y, game_map, monsters)
    elif input_moving == 'D':
        player_finished_turn = determine_action_type(player, player.x + 1, player.y, game_map, monsters)
    elif input_moving == 'P':
        player_finished_turn = True
    elif input_moving == 'I':
        print_inventory(player.inventory)

    game_map[player.x][player.y].tile = Cell.PLAYER
    return player_finished_turn
