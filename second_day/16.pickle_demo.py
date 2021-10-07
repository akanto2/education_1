'''
    file = open('./Data/zen_of_python.txt', 'w')
    file.write('추가적으로 라인을 추가합니다.  \n')
    file.close()
'''

import pickle

file = open('../Data/zen_of_python.txt', 'r')

list_of_line = file.readlines()
list_of_line.append('추가적으로 라인을 추가합니다.  \n')
file.close()

pickled_file = open('../Data/task.pickle', 'wb')
pickle.dump(list_of_line, pickled_file)

print('file pickled..')
