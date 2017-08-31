def open_and_print_file(file_name):
    file = open(file_name, 'r')
    for line in file.readlines():
        print(line.strip())
    file.close()



