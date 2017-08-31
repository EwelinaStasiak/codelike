from random import randint

from fight import deal_damage, test_for_hit, end_game
from game_map import Tile


class Monster:
    RAGING_NERD = 'Raging nerd'
    SYSOP = 'Sysop'

    def __init__(self, x, y, monster_type):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        if monster_type == Monster.RAGING_NERD:
            self.health = 10
            self.damage = 2
            self.defense = 2
            self.to_hit = 5
            self.drop_rarity = 1
            self.tile_type = Tile.RAGING_NERD
        elif monster_type == Monster.SYSOP:
            self.health = 15
            self.damage = 4
            self.defense = 4
            self.to_hit = 7
            self.drop_rarity = 4
            self.tile_type = Tile.SYSOP

    def attack(self, player):
        if test_for_hit(self.to_hit, player.to_hit):
            dealt_damage = deal_damage(self.damage, player.defense)
            print('{} attacked with roundhouse kick. You have lost {} health.'.format(self.monster_type, dealt_damage))
            player.health -= dealt_damage
            if player.health <= 0:
                end_game()
        else:
            print('{} missed.'.format(self.monster_type))

    def move(self, game_map):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [0, 0]]
        for i in range(4):
            direction = directions.pop(randint(0, len(directions) - 1))
            tile = game_map[self.x + direction[0]][self.y + direction[1]].tile
            if tile == Tile.EMPTY or (direction[0] == 0 and direction[1] == 0):
                game_map[self.x][self.y].tile = Tile.EMPTY
                self.x += direction[0]
                self.y += direction[1]
                game_map[self.x][self.y].tile = self.tile_type
                break


def check_if_player_is_nearby(game_map, monster_x, monster_y):
    if game_map[monster_x][monster_y - 1].tile == Tile.PLAYER:
        return True
    elif game_map[monster_x][monster_y + 1].tile == Tile.PLAYER:
        return True
    elif game_map[monster_x - 1][monster_y].tile == Tile.PLAYER:
        return True
    elif game_map[monster_x + 1][monster_y].tile == Tile.PLAYER:
        return True
    return False


def move_monsters(game_map, monsters):
    for monster in monsters:
        if not check_if_player_is_nearby(game_map, monster.x, monster.y):
            monster.move(game_map)


def monsters_attack(game_map, monsters, player):
    for monster in monsters:
        if check_if_player_is_nearby(game_map, monster.x, monster.y):
            monster.attack(player)


def create_monsters(game_map):
    monsters = []
    for column in game_map:
        for cell in column:
            if cell.tile == Tile.RAGING_NERD:
                monsters.append(Monster(cell.x, cell.y, Monster.RAGING_NERD))
            elif cell.tile == Tile.SYSOP:
                monsters.append(Monster(cell.x, cell.y, Monster.SYSOP))
    return monsters
