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


def main():
    start_screen()


if __name__ == '__main__':
    main()