class Monster:
    A = 0
    B = 1

    def __init__(self, x, y, health, damage, to_hit, defense, level):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.to_hit = to_hit
        self.defense = defense
        self.level = level

    def attack(self):
        pass

    def move(self):
        pass
