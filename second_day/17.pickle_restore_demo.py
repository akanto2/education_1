import pickle

file = open('../Data/task.pickle', 'rb')
list_of_line = pickle.load(file)
print(list_of_line)
