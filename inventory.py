from items import Food, Pants, Armor, Weapon


def print_inventory(inventory, messages):
    if not inventory:
        return messages.append('The inventory is empty.')
    for i in range(len(inventory)):

        if isinstance(inventory[i], Weapon):
            item_weapon = (str(i + 1) + 'Type: {} '.format(inventory[i].item_type) +
                            'Weight: {} '.format(inventory[i].weight) +
                            'Rarity: {} '.format(inventory[i].rarity) +
                            'Damage: {} '.format(inventory[i].damage) +
                            'Hit Rate: {} '.format(inventory[i].hit_rate) +
                            'Equipped: {} '.format(inventory[i].equipped))
            messages.append(item_weapon)

        elif isinstance(inventory[i], Armor):
            item_armor = (str(i + 1) + 'Type {} '.format(inventory[i].item_type) +
                            'Weight: {} '.format(inventory[i].weight) +
                            'Rarity: {} '.format(inventory[i].rarity) +
                            'Defense: {} '.format(inventory[i].defense) +
                            'Hit Points: {} '.format(inventory[i].hit_points) +
                            'Equipped: {} '.format(inventory[i].equipped))
            messages.append(item_armor)

        elif isinstance(inventory[i], Pants):
            item_pants = (str(i + 1) + 'Type: {} '.format(inventory[i].item_type) +
                            'Weight: {} '.format(inventory[i].weight) +
                            'Rarity: {} '.format(inventory[i].rarity) +
                            'Defense: {} '.format(inventory[i].defense) +
                            'Equipped: {} '.format(inventory[i].equipped))
            messages.append(item_pants)

        elif isinstance(inventory[i], Food):
            item_food = (str(i + 1) + 'Type: {} '.format(inventory[i].item_type) +
                            'Weight: {} '.format(inventory[i].weight) +
                            'Rarity: {} '.format(inventory[i].rarity) +
                            'Heal Amount: {} '.format(inventory[i].heal_amount) +
                            'Equipped: {} '.format(inventory[i].equipped))
            messages.append(item_food)
    for message in messages:
        print(message)
    messages.clear()


def add_item(item, inventory, messages):
    total_weight = 0
    for element in inventory:
        total_weight += element.weight
    if total_weight + item.weight <= 50:
        return inventory.append(item)
    else:
        messages.append("You can not add this item because the equipment would be too heavy.")


def use_item(player):
    number_item = int(input('Press number item which you want to use:'))# trzeba dodać żeby dało się tylko wpisac numer
    item_to_use = player.inventory[number_item - 1]
    if isinstance(item_to_use, Food):
        player.health += item_to_use.heal_amount
        player.inventory.remove(player.inventory[number_item - 1])
    else:
        for item in player.inventory:
            if item.equipped and item_to_use.item_type == item.item_type:
                item_to_use.equipped = True
                item.equipped = False
