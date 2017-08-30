from items import *


def print_inventory(inventory):
    for item in inventory:
        if isinstance(item, Weapon):
            print("Type: {}".format(item.weapon_type), "Weight: {}".format(item.weight), "Rarity: {}".format(item.rarity),
                  "Damage: {}".format(item.damage), "Hit Rate: {}".format(item.hit_rate))
        elif isinstance(item, Armor):
            print("Type {}".format(item.armor_type), "Weight: {}".format(item.weight), "Rarity: {}".format(item.rarity),
                  "Defense: {}".format(item.defense), "Hit Points: {}".format(item.hit_points))
        elif isinstance(item, Pants):
            print("Type: {}".format(item.pants_type), "Weight: {}".format(item.weight), "Rarity: {}".format(item.rarity),
                  "Defense: {}".format(item.defense))

        elif isinstance(item, Food):
            print("Type: {}".format(item.food_type), "Weight: {}".format(item.weight), "Rarity: {}".format(item.rarity),
                  "Heal Amount: {}".format(item.heal_amount))


def add_item(inventory):
    return inventory.append(create_item(4))
