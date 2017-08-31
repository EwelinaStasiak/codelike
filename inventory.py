from items import Food, Pants, Armor, Weapon


def print_inventory(inventory, messages):
    if not inventory:
        return messages.append('The inventory is empty.')
    for i in range(len(inventory)):

        if isinstance(inventory[i], Weapon):
            item_weapon = ('{}. '.format(i + 1) + ' Type:{} '.format(inventory[i].item_type) +
                           ' Weight:{} '.format(inventory[i].weight) +
                           ' Damage:{} '.format(inventory[i].damage) +
                           ' Hit Rate:{} '.format(inventory[i].hit_rate) +
                           ' Equipped:{} '.format(inventory[i].equipped))
            messages.append(item_weapon)
        elif isinstance(inventory[i], Armor):
            item_armor = ('{}. '.format(i + 1) + ' Type{} '.format(inventory[i].item_type) +
                          ' Weight:{} '.format(inventory[i].weight) +
                          ' Defense:{} '.format(inventory[i].defense) +
                          ' Equipped:{} '.format(inventory[i].equipped))
            messages.append(item_armor)
        elif isinstance(inventory[i], Pants):
            item_pants = ('{}. '.format(i + 1) + ' Type:{} '.format(inventory[i].item_type) +
                          ' Weight:{} '.format(inventory[i].weight) +
                          ' Defense:{} '.format(inventory[i].defense) +
                          ' Equipped:{} '.format(inventory[i].equipped))
            messages.append(item_pants)
        elif isinstance(inventory[i], Food):
            item_food = ('{}. '.format(i + 1) + ' Type:{} '.format(inventory[i].item_type) +
                         ' Weight:{} '.format(inventory[i].weight) +
                         ' Heal Amount:{} '.format(inventory[i].heal_amount))
            messages.append(item_food)
    for message in messages:
        print(message)
    print('')
    messages.clear()


def add_item(item, inventory, messages):
    total_weight = 0
    weight_limit = 25
    for element in inventory:
        total_weight += element.weight
    if total_weight + item.weight <= weight_limit:
        messages.append('You received an item')
        return inventory.append(item)
    else:
        messages.append("You can not add this item because the equipment would be too heavy.")


def destroy_item(player, messages):
    index = input('Which item you want to destroy ?\n')
    if index.isdigit():
        if int(index) <= len(player.inventory):
            player.inventory.remove(player.inventory[int(index) - 1])
            messages.append('Item destroyed')
            return
    messages.append('Invalid input')
    return


def use_item(player):
    # trzeba dodać żeby dało się tylko wpisac numer
    number_item = int(input('Press number item which you want to use:\n'))
    if isinstance(player.inventory[number_item - 1], Food):
        player.health += player.inventory[number_item - 1].heal_amount
        player.inventory.remove(player.inventory[number_item - 1])
    else:
        equipped_item_found = False
        for item in player.inventory:
            if item.__class__ == player.inventory[number_item - 1].__class__ and item.equipped:
                equipped_item_found = True
                break
        if equipped_item_found:
            for item in player.inventory:
                if item.__class__ == player.inventory[number_item - 1].__class__ and item.equipped:
                    item.equipped = False
                    player.inventory[number_item - 1].equipped = True
                    break
        else:
            player.inventory[number_item - 1].equipped = True
