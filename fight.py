from random import randint
from screens import *


def test_for_hit(to_hit, evade):
    attacker_result = 0
    defender_result = 0
    for i in range(to_hit):
        attacker_result += randint(1, 4)
    for i in range(evade):
        defender_result += randint(1, 3)
    return attacker_result >= defender_result


def deal_damage(damage, defense):
    total_damage = 0
    for i in range(damage):
        total_damage += randint(1, 2)
    if total_damage - defense < 1:
        return 1
    else:
        return total_damage - defense


def end_game():
    print('You have died')
    open_and_print_file('lose_screen.txt')
