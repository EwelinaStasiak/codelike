from game_map import *


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


def moving_player(game_map, player_location):
    player_x = player_location[0]
    player_y = player_location[1]
    print('Press W(up), S(down), A(left), D(right)')
    while True:
        input_moving = getch()
        if input_moving.upper() == 'W':

            if game_map[player_x][player_y-1].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_y -= 1
        elif input_moving.upper() == 'S':
            if game_map[player_x][player_y + 1].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_y += 1
        elif input_moving.upper() == 'A':
            if game_map[player_x - 1][player_y].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_x -= 1
        elif input_moving.upper() == 'D':
            if game_map[player_x + 1][player_y].tile != Tile.WALL:
                game_map[player_x][player_y].tile = Tile.EMPTY
                player_x += 1

        game_map[player_x][player_y].tile = Tile.PLAYER
        print_map(game_map)













