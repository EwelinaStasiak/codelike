import os

from fight import end_game
from game_map import import_map_from_file as create_map
from game_map import print_map
from game_map import search_for_player
from player import action_of_player, Player, check_input
from monster import create_monsters, move_monsters, monsters_attack
from screens import open_and_print_file


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


def add_highscore(player):
    name = input('Please enter your name.\n')
    highscore = 'Name:{} / KillCount:{} / Health:{} / HeroType:{} \n'.format(
        name, player.kill_count, player.health, player.type_hero)
    if not os.path.isfile('highscores.txt'):
        open('highscores.txt', "a").close()
    with open('highscores.txt', "a") as file:
        file.write(highscore)


def main():
    files = ['level_.txt', 'example_level.txt', 'boss.txt']
    level = 0
    game_map = create_map(files[level])
    monsters = create_monsters(game_map)
    player_location = search_for_player(game_map)
    player = start_screen(player_location)

    os.system('cls' if os.name == 'nt' else 'clear')
    print_map(game_map)
    messages = []
    move_to_next_level = []
    while player.health > 0:
        player_input = getch().upper()
        if check_input(player_input, game_map, player, messages):
            action_of_player(player_input, game_map, player, monsters, messages, move_to_next_level)
            move_monsters(game_map, monsters)
            monsters_attack(game_map, monsters, player, messages)
            if move_to_next_level:
                move_to_next_level.clear()
                game_map.clear()
                level += 1
                game_map = create_map(files[level])
                monsters = create_monsters(game_map)
                player_location = search_for_player(game_map)
                player.x = player_location[0]
                player.y = player_location[1]
        os.system('cls' if os.name == 'nt' else 'clear')
        print_map(game_map)
        if messages:
            for message in messages:
                print(message)
            messages.clear()
        if player.end_game:
            break
    if player.health < 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        input('You have died. Hit enter')
        os.system('cls' if os.name == 'nt' else 'clear')
        end_game()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        add_highscore(player)
        open_and_print_file('win_screen.txt')


def play_screen(player_location):
    os.system('cls' if os.name == 'nt' else 'clear')
    open_and_print_file('story_screen.txt')
    input('Hit enter to continue')
    os.system('cls' if os.name == 'nt' else 'clear')
    open_and_print_file('choose_character.txt')
    while True:
        choose_character = input().upper()
        if choose_character == 'H':
            return Player(player_location[0], player_location[1], Player.HENRYK)
        elif choose_character == 'Z':
            return Player(player_location[0], player_location[1], Player.ZDZISLAW)
        elif choose_character == 'E':
            return False
        else:
            print('You can enter only H(enryk) or Z(dzisław) or E(xit)')


def help_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    open_and_print_file('help_screen.txt')
    print("You are in help")
    while True:
        inp = input("Type E to exit").lower()
        if inp == 'e':
            return


def lose_screen():
    open_and_print_file('lose_screen.txt')


def win_screen():
    print(open_and_print_file('win_screen.txt'))


def hall_of_fame_screen():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('This brave souls saved the world:\n')
        if os.path.isfile('highscores.txt'):
            open_and_print_file('highscores.txt')
        else:
            print('The world was not saved yet :( ')
        inp = input("\nType E to exit").lower()
        if inp == 'e':
            break


def exit_game():
    exit()


def start_screen(player_location):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        open_and_print_file('StartScreen.txt')
        decision = input().lower()
        if decision == 'p':
            character = play_screen(player_location)
            if character:
                return character
        elif decision == 'l':
            hall_of_fame_screen()
        elif decision == 'h':
            help_screen()
        elif decision == 'e':
            exit_game()
        else:
            print('You can type only P, H, L or E !')


if __name__ == '__main__':
    main()
