class Cell:
    WALL = '#'
    EMPTY = '.'
    PLAYER = '@'
    RAGING_NERD = 'A'
    SYSOP = 'B'

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
