from game_map import import_map_from_file as create_map
from game_map import print_map
from game_map import search_for_player
from player import moving_player
from monster import create_monsters


def main():
    game_map = create_map('example_level.txt')
    print_map(game_map)
    player_location = search_for_player(game_map)
    monsters = create_monsters
    moving_player(game_map, player_location)
    # start_screen()


def play_screen():
    print('Play a game')


def help_screen():
    print('help')


def lose_screen():
    pass


def win_screen():
    pass


def hall_of_fame_screen():
    print('blabla')


def exit_game():
    exit()


def start_screen():
    while True:
        decision = input('Enter P or H or L or E').lower()
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
