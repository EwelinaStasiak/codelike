#import os.path

#scriptpath = os.path.dirname(__file__)
#filename = os.path.join(scriptpath, 'choose_character.txt')


def open_file(file_name):
    file = open(file_name, 'r')
    for line in file.readlines():
        print(line.strip())
    file.close()



