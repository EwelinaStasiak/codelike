from random import randint


class Weapon:
    CHAIR = 'Chair'
    MOUSE = 'Mouse'
    TABLE = 'Table'

    def __init__(self, weight, rarity, damage, hit_rate, item_type):
        self.weight = weight
        self.rarity = rarity
        self.damage = damage
        self.hit_rate = hit_rate
        self.item_type = item_type


class Armor:
    JACKET = 'Jacket'
    TSHIRT = 'T-shirt'
    SWEATSHIRT = 'Sweatshirt'

    def __init__(self, weight, rarity, defense, hit_points, item_type):
        self.weight = weight
        self.rarity = rarity
        self.defense = defense
        self.hit_points = hit_points
        self.item_type = item_type


class Pants:
    SKIRT = 'Skirt'
    JEANS = 'Jeans'
    SHORTS = 'Shorts'

    def __init__(self, weight, rarity, defense, item_type):
        self.weight = weight
        self.rarity = rarity
        self.defense = defense
        self.item_type = item_type


class Food:
    DONUT = 'Donut'
    COFFEE = 'Coffee'

    def __init__(self, weight, rarity, heal_amount, item_type):
        self.weight = weight
        self.rarity = rarity
        self.heal_amount = heal_amount
        self.item_type = item_type

    def use(self):
        pass


def rarity_bonus(rarity, chance_for_bonus):
    bonus = 0
    for i in range(rarity):
        if randint(1, 100) <= chance_for_bonus:
            bonus += 1
    return bonus


def create_weapon(rarity):
    r = randint(1, 99)
    damage_bonus = rarity_bonus(rarity, 35)
    hit_rate_bonus = rarity_bonus(rarity, 50)
    if r <= 33:
        weight = 2
        damage = 2 + damage_bonus
        hit_rate = 5 + hit_rate_bonus
        return Weapon(weight, rarity, damage, hit_rate, Weapon.MOUSE)
    elif 33 < r <= 66:
        weight = 4
        damage = 3 + damage_bonus
        hit_rate = 4 + hit_rate_bonus
        return Weapon(weight, rarity, damage, hit_rate, Weapon.CHAIR)
    else:
        weight = 7
        damage = 6 + damage_bonus
        hit_rate = 2 + hit_rate_bonus
        return Weapon(weight, rarity, damage, hit_rate, Weapon.TABLE)


def create_armor(rarity):
    r = randint(1, 99)
    defense_bonus = rarity_bonus(rarity, 40)
    health_bonus = rarity_bonus(rarity, 60)
    if r <= 33:
        weight = 1
        defense = 2 + defense_bonus
        health = 3 + health_bonus
        return Armor(weight, rarity, defense, health, Armor.TSHIRT)
    elif 33 < r <= 66:
        weight = 3
        defense = 2 + defense_bonus
        health = 3 + health_bonus
        return Armor(weight, rarity, defense, health, Armor.SWEATSHIRT)
    else:
        weight = 5
        defense = 2 + defense_bonus
        health = 3 + health_bonus
        return Armor(weight, rarity, defense, health, Armor.JACKET)


def create_pants(rarity):
    defense_bonus = rarity_bonus(rarity, 30)

    r = randint(1, 99)
    if r <= 33:
        weight = 2
        defense = 1 + defense_bonus
        return Pants(weight, rarity, defense, Pants.SHORTS)
    elif 33 < r <= 66:
        weight = 4
        defense = 2 + defense_bonus
        return Pants(weight, rarity, defense, Pants.SKIRT)
    else:
        weight = 6
        defense = 3 + defense_bonus
        return Pants(weight, rarity, defense, Pants.JEANS)


def create_equipment(rarity):
    r = randint(1, 99)
    if r <= 33:
        return create_weapon(rarity)
    elif 33 < r <= 66:
        return create_armor(rarity)
    else:
        return create_pants(rarity)


def create_consumable(rarity):
    r = randint(1, 100)
    weight = 2
    if r <= 50:
        food_type = Food.DONUT
        heal_amount = rarity * 2
    else:
        food_type = Food.COFFEE
        heal_amount = rarity * 3

    return Food(weight, rarity, heal_amount, food_type)


def create_item(rarity):
    r = randint(1, 100)
    if r < 60:
        return create_equipment(rarity)
    else:
        return create_consumable(rarity)
