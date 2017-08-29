from enum import Enum


class Tile(Enum):
    WALL = '#'
    EMPTY = '.'
    PLAYER = '@'


class Cell:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile


def create_empty_map(width=50, height=20):
    game_map = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(Cell(x, y, Tile.EMPTY))
        game_map.append(column)
    return game_map


def determine_tile_type(character):
    if character == Tile.WALL.value:
        return Tile.WALL
    elif character == Tile.EMPTY.value:
        return Tile.EMPTY
    elif character == Tile.PLAYER.value:
        return Tile.PLAYER
    else:
        return Tile.EMPTY


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


def print_map(game_map):
    row = []
    for i in range(len(game_map[0])):
        row.append([])
        for j in range(len(game_map)):
            row[i].append(game_map[j][i].tile.value)
        print(''.join(row[i]))


def search_for_player(game_map):
    for column in game_map:
        for cell in column:
            if cell.tile == Tile.PLAYER:
                return [cell.x, cell.y]
