import inventory
from fight import test_for_hit, deal_damage
from game_map import *
from inventory import *
from items import create_item
from boss_game import *


class Player:
    ZDZISLAW = 'Zdzisław'
    HENRYK = 'Henryk'

    def __init__(self, x, y, type_hero):
        self.type_hero = type_hero
        self.x = x
        self.y = y
        self.inventory = []
        self.kill_count = 0
        self.end_game = False

        if type_hero == Player.ZDZISLAW:
            self.health = 35
            self.damage = 7
            self.defense = 2
            self.agility = 5
        elif type_hero == Player.HENRYK:
            self.health = 40
            self.damage = 5
            self.defense = 4
            self.agility = 5

    def attack(self, monsters, monster, messages, game_map):
        weapon = self.get_equipped_item_stats(Weapon)
        if test_for_hit(self.agility + weapon[2], monster.agility):
            dealt_damage = deal_damage(self.damage + weapon[1], monster.defense)
            messages.append(
                'You attacked {} with {}. You dealt {} damage. The blood is everywhere'.format(
                    monster.monster_type, weapon[0], dealt_damage))
            monster.health -= dealt_damage
            if monster.health <= 0:
                messages.append('The {} died in agony.'.format(monster.monster_type))
                game_map[monster.x][monster.y].tile = Cell.EMPTY
                loot = create_item(monster.drop_rarity)
                inventory.add_item(loot, self.inventory, messages)
                self.kill_count += 1
                monsters.remove(monster)
        else:
            messages.append('You missed {}.'.format(monster.monster_type))

    def get_equipped_item_stats(self, type_of_item):
        for item in self.inventory:
            if item.__class__ == type_of_item and item.equipped:
                if type_of_item == Weapon:
                    return [item.item_type, item.damage, item.agility]
                if type_of_item == Armor or type_of_item == Pants:
                    return [item.item_type, item.defense]
        return ['Spoon', 0, 0]


def search_for_monster(monsters, new_x, new_y):
    for monster in monsters:
        if monster.x == new_x and monster.y == new_y:
            return monster


def print_status(player, messages):
    messages.append('Hero type:{}  Health:{}  Damage:{}  Defense:{}  Agility:{}  KillCount: {}'.format(
        player.type_hero, player.health, player.damage, player.defense, player.agility, player.kill_count))


def check_input(player_input, game_map, player, messages):
    new_x = player.x
    new_y = player.y
    input_for_moving = False
    if player_input == 'W':
        new_y -= 1
        input_for_moving = True
    elif player_input == 'S':
        new_y += 1
        input_for_moving = True
    elif player_input == 'A':
        new_x -= 1
        input_for_moving = True
    elif player_input == 'D':
        new_x += 1
        input_for_moving = True
    elif player_input == 'P':
        return True
    elif player_input == 'I':
        while True:
            print_inventory(player.inventory, messages)
            if not player.inventory:
                break
            decision = input('(U)se item, (D)elete item, Any other to exit\n').upper()
            if decision == 'U':
                use_item(player)
                break
            elif decision == 'D':
                destroy_item(player, messages)
                break
            else:
                break
    elif player_input == 'O':
        print_status(player, messages)
    if input_for_moving:
        tile = game_map[new_x][new_y].tile
        if tile == Cell.EMPTY or tile == Cell.RAGING_NERD or tile == Cell.SYSOP \
                or tile == Cell.STAIRS or tile == Cell.HOT_GAME:
            return True
    return False


def determine_action_type(player, new_x, new_y, game_map, monsters, messages, move_to_next_level):
    if game_map[new_x][new_y].tile == Cell.EMPTY:
        game_map[player.x][player.y].tile = Cell.EMPTY
        player.x = new_x
        player.y = new_y
        game_map[player.x][player.y].tile = Cell.PLAYER
        return True
    elif game_map[new_x][new_y].tile == Cell.RAGING_NERD or game_map[new_x][new_y].tile == Cell.SYSOP:
        monster = search_for_monster(monsters, new_x, new_y)
        player.attack(monsters, monster, messages, game_map)
        return True
    elif game_map[new_x][new_y].tile == Cell.STAIRS:
        if monsters:
            messages.append('You need to kill all monsters to use the stairs.')
            return False
        else:
            move_to_next_level.append(True)
            messages.append('You moved to the next level')
            return True
    elif game_map[new_x][new_y].tile == Cell.HOT_GAME:
        print('Play HOT - WARM - COLD game. ')
        print('If you guess a three-digit number.')
        print('I\'ll give you a super important secret paper and you close the portal to your world.')
        play_a_hot_game(player)


def action_of_player(player_input, game_map, player, monsters, messages, move_to_next_level):
    player_finished_turn = False
    if player_input == 'W':
        player_finished_turn = determine_action_type(
            player, player.x, player.y - 1, game_map, monsters, messages, move_to_next_level)
    elif player_input == 'S':
        player_finished_turn = determine_action_type(
            player, player.x, player.y + 1, game_map, monsters, messages, move_to_next_level)
    elif player_input == 'A':
        player_finished_turn = determine_action_type(
            player, player.x - 1, player.y, game_map, monsters, messages, move_to_next_level)
    elif player_input == 'D':
        player_finished_turn = determine_action_type(
            player, player.x + 1, player.y, game_map, monsters, messages, move_to_next_level)
    elif player_input == 'P':
        player_finished_turn = True

    game_map[player.x][player.y].tile = Cell.PLAYER
    return player_finished_turn
