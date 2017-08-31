class Cell:
    WALL = '#'
    EMPTY = '.'
    PLAYER = '@'
    RAGING_NERD = 'A'
    SYSOP = 'B'
    STAIRS = '<'
    BOSS_1 = '\''
    BOSS_2 = '-'
    BOSS_3 = '('
    BOSS_4 = ')'
    BOSS_5 = ' '
    BOSS_6 = '_'
    BOSS_7 = '|'
    BOSS_8 = '\\'
    BOSS_9 = '/'
    BOSS_10 = 'p'
    BOSS_11 = 'a'
    BOSS_12 = 's'
    BOSS_13 = 'w'
    BOSS_14 = 'o'
    BOSS_15 = 'r'
    BOSS_16 = 'd'
    HOT_GAME = '*'

    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile


def create_empty_map(width=50, height=20):
    game_map = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(Cell(x, y, Cell.EMPTY))
        game_map.append(column)
    return game_map


def determine_tile_type(character):
    if character == Cell.WALL:
        return Cell.WALL
    elif character == Cell.EMPTY:
        return Cell.EMPTY
    elif character == Cell.PLAYER:
        return Cell.PLAYER
    elif character == Cell.RAGING_NERD:
        return Cell.RAGING_NERD
    elif character == Cell.SYSOP:
        return Cell.SYSOP
    elif character == Cell.STAIRS:
        return Cell.STAIRS
    elif character == Cell.BOSS_1S_1:
        return Cell.BOSS_1
    elif character == Cell.BOSS_2:
        return Cell.BOSS_2
    elif character == Cell.BOSS_3:
        return Cell.BOSS_3
    elif character == Cell.BOSS_4:
        return Cell.BOSS_4
    elif character == Cell.BOSS_5:
        return Cell.BOSS_5
    elif character == Cell.BOSS_6:
        return Cell.BOSS_6
    elif character == Cell.BOSS_7:
        return Cell.BOSS_7
    elif character == Cell.BOSS_8:
        return Cell.BOSS_8
    elif character == Cell.BOSS_9:
        return Cell.BOSS_9
    elif character == Cell.BOSS_10:
        return Cell.BOSS_10
    elif character == Cell.BOSS_11:
        return Cell.BOSS_11
    elif character == Cell.BOSS_12:
        return Cell.BOSS_12
    elif character == Cell.BOSS_13:
        return Cell.BOSS_13
    elif character == Cell.BOSS_14:
        return Cell.BOSS_14
    elif character == Cell.BOSS_15:
        return Cell.BOSS_15
    elif character == Cell.BOSS_16:
        return Cell.BOSS_16
    elif character == Cell.HOT_GAME:
        return Cell.HOT_GAME
    else:
        return Cell.EMPTY


def import_map_from_file(filename):
    game_map = create_empty_map()
    with open(filename, 'r') as file:
        line_count = 0
        for line in file:
            row = list(line.replace('\n', ''))
            for i in range(len(row)):
                game_map[i][line_count].tile = determine_tile_type(row[i])
            line_count += 1
    return game_map


def color_tile(tile):
    if tile == Cell.PLAYER:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.RAGING_NERD:
        return '\x1b[1;31;40m' + tile + '\x1b[0m'
    if tile == Cell.SYSOP:
        return '\x1b[1;31;40m' + tile + '\x1b[0m'
    if tile == Cell.EMPTY:
        return '\x1b[0;35;40m' + tile + '\x1b[0m'
    if tile == Cell.WALL:
        return '\x1b[0;34;40m' + tile + '\x1b[0m'
    if tile == Cell.STAIRS:
        return '\x1b[0;36;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_1:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_2:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_3:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_4:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_5:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_6:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_7:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_8:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_9:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_10:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_11:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_12:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_13:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_14:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_15:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.BOSS_16:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    if tile == Cell.HOT_GAME:
        return '\x1b[1;36;40m' + tile + '\x1b[0m'


def print_map(game_map):
    row = []
    for i in range(len(game_map[0])):
        row.append([])
        for j in range(len(game_map)):
            row[i].append(color_tile(game_map[j][i].tile))
        print(''.join(row[i]))


def search_for_player(game_map):
    for column in game_map:
        for cell in column:
            if cell.tile == Cell.PLAYER:
                return [cell.x, cell.y]
