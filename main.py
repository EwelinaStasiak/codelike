import os

from game_map import import_map_from_file as create_map
from game_map import print_map
from game_map import search_for_player
from player import action_of_player, Player, check_input
from monster import create_monsters, move_monsters, monsters_attack
from screens import open_file


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    start_screen()
    game_map = create_map('example_level.txt')
    monsters = create_monsters(game_map)
    player_location = search_for_player(game_map)
    player = Player(player_location[0], player_location[1], Player.ZDZISLAW)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_map(game_map)
    messages = []
    while True:
        player_input = getch().upper()
        if check_input(player_input, game_map, player, messages):
            action_of_player(player_input, game_map, player, monsters, messages)
            move_monsters(game_map, monsters)
            monsters_attack(game_map, monsters, player, messages)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_map(game_map)
        if messages:
            for message in messages:
                print(message)
            messages.clear()


def play_screen():
    pass


def help_screen():
    pass


def lose_screen():
    pass


def win_screen():
    print(open_file('win_screen.txt'))


def hall_of_fame_screen():
    print('blabla')


def exit_game():
    exit()


def start_screen():
    open_file('StartScreen.txt')
    while True:
        decision = input().lower()
        if decision == 'p':
            play_screen()
            break
        elif decision == 'l':
            hall_of_fame_screen()
            break
        elif decision == 'h':
            help_screen()
            break
        elif decision == 'e':
            exit_game()
        else:
            print('You can type only P, H, L or E !')


if __name__ == '__main__':
    main()
