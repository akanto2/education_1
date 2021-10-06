try:
    file = open('./Data/not_exist.txt', 'r')
    file.readlines()
    file.close()
except FileNotFoundError:
    print('no file')

