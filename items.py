from random import randint


class Weapon:
    CHAIR = 'Chair'
    MOUSE = 'Mouse'
    TABLE = 'Table'

    def __init__(self, weight, damage, agility, item_type):
        self.weight = weight
        self.damage = damage
        self.agility = agility
        self.item_type = item_type
        self.equipped = False


class Armor:
    JACKET = 'Jacket'
    TSHIRT = 'T-shirt'
    SWEATSHIRT = 'Sweatshirt'

    def __init__(self, weight, defense, item_type):
        self.weight = weight
        self.defense = defense
        self.item_type = item_type
        self.equipped = False


class Pants:
    SKIRT = 'Skirt'
    JEANS = 'Jeans'
    SHORTS = 'Shorts'

    def __init__(self, weight, defense, item_type):
        self.weight = weight
        self.defense = defense
        self.item_type = item_type
        self.equipped = False


class Food:
    DONUT = 'Donut'
    COFFEE = 'Coffee'

    def __init__(self, weight, heal_amount, item_type):
        self.weight = weight
        self.heal_amount = heal_amount
        self.item_type = item_type
        self.equipped = False

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
    agility_bonus = rarity_bonus(rarity, 50)
    if r <= 33:
        weight = 2
        damage = 2 + damage_bonus
        agility = 5 + agility_bonus
        return Weapon(weight, damage, agility, Weapon.MOUSE)
    elif 33 < r <= 66:
        weight = 4
        damage = 3 + damage_bonus
        agility = 4 + agility_bonus
        return Weapon(weight, damage, agility, Weapon.CHAIR)
    else:
        weight = 7
        damage = 6 + damage_bonus
        agility = 2 + agility_bonus
        return Weapon(weight, damage, agility, Weapon.TABLE)


def create_armor(rarity):
    r = randint(1, 99)
    defense_bonus = rarity_bonus(rarity, 40)
    if r <= 33:
        weight = 1
        defense = 2 + defense_bonus
        return Armor(weight, defense, Armor.TSHIRT)
    elif 33 < r <= 66:
        weight = 3
        defense = 2 + defense_bonus
        return Armor(weight, defense, Armor.SWEATSHIRT)
    else:
        weight = 5
        defense = 2 + defense_bonus
        return Armor(weight, defense, Armor.JACKET)


def create_pants(rarity):
    defense_bonus = rarity_bonus(rarity, 30)

    r = randint(1, 99)
    if r <= 33:
        weight = 2
        defense = 1 + defense_bonus
        return Pants(weight, defense, Pants.SHORTS)
    elif 33 < r <= 66:
        weight = 4
        defense = 2 + defense_bonus
        return Pants(weight, defense, Pants.SKIRT)
    else:
        weight = 6
        defense = 3 + defense_bonus
        return Pants(weight, defense, Pants.JEANS)


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

    return Food(weight, heal_amount, food_type)


def create_item(rarity):
    r = randint(1, 100)
    if r < 60:
        return create_equipment(rarity)
    else:
        return create_consumable(rarity)
