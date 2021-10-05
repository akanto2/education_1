my_str = 'Hello world'

# in, not in 연산자 -> bool 값을 반환
result = 'llo' in my_str
print(result)

result2 = 'He' not in my_str
print(result2)

# upper() lower() isupper() islower()
print(type(my_str))
print(my_str.upper())
print(my_str.lower())
print(my_str.islower())

# startswith(), endswith()
startswith_str = 'http://www.naver.com/'
endswith_str = 'flower.jpg'

print(startswith_str.startswith('http'))
print(endswith_str.endswith('.jpg'))

# split()
split_str = 'red,blue,white,purple,tan,black'
colors = split_str.split(',')
print(colors)

split_str2 = 'red|blue|white|purple|tan|black'
colors2 = split_str2.split('|')
print(colors2)
print(type(colors))
