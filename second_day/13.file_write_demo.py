def main():
    file = open('../Data/test_write.txt', 'w')

    file.write('test test test\n')
    file.write('한글 테스트 입니다.\n')

    file.close()

    # list of line
    lines = [
        'abc',
        'def',
        '가나다'
    ]
    # 각 라인별로 \n 문자 추가
    lines_with_new_line = []
    for line in lines:
        lines_with_new_line.append(line + '\n')

    file2 = open('../Data/test_write.txt', 'w')
    file2.writelines(lines_with_new_line)
    file2.close()
    print('job comleted..')


if __name__ == '__main__':
    main()
