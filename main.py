from game_map import import_map_from_file as create_map
from game_map import print_map


def main():
    print_map(create_map('example_level.txt'))


if __name__ == "__main__":
    main()
