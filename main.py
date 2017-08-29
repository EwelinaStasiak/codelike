from game_map import import_map_from_file as create_map
from game_map import print_map
from game_map import search_for_player


def main():
    game_map = create_map('example_level.txt')
    print_map(game_map)
    player_location = search_for_player(game_map)
    print(player_location)
    # start_screen()


def play_screen():
    print("Play a game")


def help_screen():
    print("help")


def lose_screen():
    pass


def win_screen():
    pass


def hall_of_fame_screen():
    print("blabla")


def exit_game():
    exit()


def start_screen():
    while True:
        decision = input("Enter P or H or L or E")
        if decision.lower() == ("P").lower():
            play_screen()
            break
        elif decision.lower() == ("L").lower():
            hall_of_fame_screen()
            break
        elif decision.lower() == ("H").lower():
            help_screen()
            break
        elif decision.lower() == ("E").lower():
            exit_game()
        else:
            print("You can select only P or H or L")


if __name__ == '__main__':
    main()
