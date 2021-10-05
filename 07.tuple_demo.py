# Tuple은 괄호를 리터럴 기호로 사용
my_tuple = 'red', 'blue', 'orange'

print(type(my_tuple))

# destruction, 구조분해
a, b, c = my_tuple

print(a)

# indexting, slicing 은 List와 동일
print(my_tuple[2])
print(my_tuple[0:3])
