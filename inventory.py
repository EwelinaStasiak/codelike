from items import *


def print_inventory(inventory):
    for i in range(len(inventory)):

        if isinstance(inventory[i], Weapon):
            print(str(i + 1), "Type: {}".format(inventory[i].weapon_type), "Weight: {}".format(inventory[i].weight), "Rarity: {}".format(inventory[i].rarity),
                  "Damage: {}".format(inventory[i].damage), "Hit Rate: {}".format(inventory[i].hit_rate))
        elif isinstance(inventory[i], Armor):
            print(str(i + 1), "Type {}".format(inventory[i].armor_type), "Weight: {}".format(inventory[i].weight), "Rarity: {}".format(inventory[i].rarity),
                  "Defense: {}".format(inventory[i].defense), "Hit Points: {}".format(inventory[i].hit_points))
        elif isinstance(inventory[i], Pants):
            print(str(i + 1), "Type: {}".format(inventory[i].pants_type), "Weight: {}".format(inventory[i].weight), "Rarity: {}".format(inventory[i].rarity),
                  "Defense: {}".format(inventory[i].defense))

        elif isinstance(inventory[i], Food):
            print(str(i + 1), "Type: {}".format(inventory[i].food_type), "Weight: {}".format(inventory[i].weight), "Rarity: {}".format(inventory[i].rarity),
                  "Heal Amount: {}".format(inventory[i].heal_amount))


def add_item(inventory):
    return inventory.append(create_item(4))

def use_item(inventory):
    pass
