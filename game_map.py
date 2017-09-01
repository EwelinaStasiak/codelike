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


def import_map_from_file(filename):
    game_map = create_empty_map()
    with open(filename, 'r') as file:
        line_count = 0
        for line in file:
            row = list(line.replace('\n', ''))
            for i in range(len(row)):
                game_map[i][line_count].tile = row[i]
            line_count += 1
    return game_map


def color_tile(tile):
    if tile == Cell.PLAYER:
        return '\x1b[1;32;40m' + tile + '\x1b[0m'
    elif tile == Cell.RAGING_NERD:
        return '\x1b[1;31;40m' + tile + '\x1b[0m'
    elif tile == Cell.SYSOP:
        return '\x1b[1;31;40m' + tile + '\x1b[0m'
    elif tile == Cell.EMPTY:
        return '\x1b[0;35;40m' + tile + '\x1b[0m'
    elif tile == Cell.WALL:
        return '\x1b[0;34;40m' + tile + '\x1b[0m'
    elif tile == Cell.STAIRS:
        return '\x1b[0;36;40m' + tile + '\x1b[0m'
    elif tile == Cell.HOT_GAME:
        return '\x1b[1;36;40m' + tile + '\x1b[0m'
    else:
        return '\x1b[1;33;40m' + tile + '\x1b[0m'


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
