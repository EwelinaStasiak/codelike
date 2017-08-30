from game_map import import_map_from_file as create_map
from game_map import print_map
from game_map import search_for_player
from player import action_of_player, Player
from monster import create_monsters, move_monsters


def main():
    game_map = create_map('example_level.txt')
    monsters = create_monsters(game_map)
    player_location = search_for_player(game_map)
    player = Player(player_location[0], player_location[1], 40, 10, 10)
    # start_screen()
    print_map(game_map)
    while True:
        if action_of_player(game_map, player):
            move_monsters(game_map, monsters, player)
        print_map(game_map)


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
