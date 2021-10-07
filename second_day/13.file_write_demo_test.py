def main():
    lines = [
        'aaa',
        'bbb',
        'ccc',
        '가나다라마바사'
    ]

    lines_with_new_line = []
    for line in lines:
        lines_with_new_line.append(line + '\n')

    file = open('../Data/test2_write.txt', 'w')
    file.writelines(lines_with_new_line)
    file.close()
    print('completed..')


if __name__ == '__main__':
    main()
