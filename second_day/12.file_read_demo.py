file = open('../Data/zen_of_python.txt', 'r')  # mode 'r'을 생략하면 default 값은 'r'이다.

lines = file.readlines()

for line in lines:
    print(line)

file.close()
