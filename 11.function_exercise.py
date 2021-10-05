def cube(number):
    """
    cube 라는 이름의 함수를 만들어서 number 라는 파라미터를 받는다.
    파라미터로 받은 숫자를 세제곱하여 반환(리턴)한다. (자기 숫자를 세번 곱한다)
    :param number:
    :return:
    """
    return number ** 3


print(cube(15))


def by_three(number=0):     # 에러가 나지 않게 하기위해 파라미터에 '=0'을 기본으로 넣는다. default 값은 0이다.
    """
    by_three 라는 두 번째 함수를 만들고 number 라는 파라미터를 받는다.
    그 숫자가 3으로 나누어지면 cube함수를 호출해서 결과를 넘겨주고, 그렇지 않으면 False 를 리턴한다.
    :param number:
    :return:
    """
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print(by_three(number=30_000_000_000_366))      # 코드에 가독성을 넣어주기위해 파라미터인 "number"을 입력해 줄 수 있다.
print(by_three())
