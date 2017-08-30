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
        elif monster_type == Monster.SYSOP:
            self.health = 15
            self.damage = 4
            self.defense = 4
            self.to_hit = 7
            self.drop_rarity = 4

    def attack(self):
        pass

    def move(self):
        pass


def create_monsters(game_map):
    monsters = []
    for column in game_map:
        for cell in column:
            if cell.tile == Tile.MONSTER:
                monsters.append(Monster(cell.x, cell.y, Monster.RAGING_NERD))
            elif cell.tile == Tile.MONSTER2:
                monsters.append(Monster(cell.x, cell.y, Monster.SYSOP))
    return monsters
