from items import *
from player import *


def print_inventory(inventory):
    for i in range(len(inventory)):

        if isinstance(inventory[i], Weapon):
            print(str(i + 1), "Type: {}".format(inventory[i].item_type), "Weight: {}".format(inventory[i].weight),
                  "Rarity: {}".format(inventory[i].rarity),
                  "Damage: {}".format(inventory[i].damage), "Hit Rate: {}".format(inventory[i].hit_rate))
        elif isinstance(inventory[i], Armor):
            print(str(i + 1), "Type {}".format(inventory[i].item_type), "Weight: {}".format(inventory[i].weight),
                  "Rarity: {}".format(inventory[i].rarity),
                  "Defense: {}".format(inventory[i].defense), "Hit Points: {}".format(inventory[i].hit_points))
        elif isinstance(inventory[i], Pants):
            print(str(i + 1), "Type: {}".format(inventory[i].item_type), "Weight: {}".format(inventory[i].weight),
                  "Rarity: {}".format(inventory[i].rarity),
                  "Defense: {}".format(inventory[i].defense))

        elif isinstance(inventory[i], Food):
            print(str(i + 1), "Type: {}".format(inventory[i].item_type), "Weight: {}".format(inventory[i].weight),
                  "Rarity: {}".format(inventory[i].rarity),
                  "Heal Amount: {}".format(inventory[i].heal_amount))


def add_item(item, inventory):
    total_weight = 0
    for element in inventory:
        total_weight += element.weight
    if total_weight + item.weight <= 50:
        return inventory.append(item)
    else:
        print("You can not add this item because the equipment would be too heavy.")


def use_item(inventory, player):
    use = input('Use item - Press U')
    if use == 'U':
        number_item = int(input('Press number item which you want to use:'))
        item_to_use = inventory[number_item - 1]
        if isinstance(item_to_use, Food):
            player.health += item_to_use.heal_amount

        else:
            for item in inventory:
                if item.equipped and item_to_use.item_type == item.item_type:
                    item_to_use.equipped = True
                    item.equipped = False
