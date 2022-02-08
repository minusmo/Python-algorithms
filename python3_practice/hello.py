firstname: str = 'Peter'
lastname: str = 'Pan'

print(firstname, lastname, end='\n')

remainder: int = 15 % 6
quotient: int = 15 // 6

print(quotient, remainder, sep=",", end="\n")
print(r'C:\path\path')
# raw string을 출력

# f string format

grade: int = 1
class_num: int = 13
attendance: int = 22

studesc: str = f'현대 고등학교 {grade}학년 {class_num}반 {attendance}번 00학생'

print(studesc)

toten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2 스텝씩 출력
print(toten[::2])
print(toten[1::2])

# 거꾸로 출력
print(toten[::-1])

# 거꾸로 정렬
toten.reverse()
print(toten)
toten.sort()
print(toten)
toten.sort(reverse=True)
print(toten)


# joined: str = '||'.join(toten)
# print(joined)

# shallow copy 뜨는 법
copy_1 = toten.copy()
copy_2 = toten[:]

print(copy_1)
print(copy_2)

# 메모리 주소 출력
print(id(copy_1))
print(id(copy_2))

# tuple 변형 불가능
tuple_1 = (1, 2)

# dictionary 만들기
d = {}
d['x'] = 1
d['y'] = 2
print(d)

d_2 = dict(a=10, b=20)

d_3 = dict([('a', 33), ('b', 55)])

print(d_2, d_3, sep="\n", end='\n')

print(d_2.keys())
print(d_3.values())

# update method는 dictionary를 override 함.
d_3.update(d_2)
print(d_3)

# 값을 가져옴
print(d_3.get('a'))

# 사전을 비움
d_2.clear()
print(d_2)

# 값 하나를 지움
d_3.pop('b')

# user input을 받음 ex)
# answer = input('1 더하기 1은?')
# print(answer)

for _ in range(0, 30, 3): # _는 loop에서 사용하지 않음을 뜻함
    print('hey')

teas = [ 'black', 'mate', 'coffee' ]
wines = [ 'bordo', 'chile', 'spain' ]
beers = [ 'sapporo', 'cass', 'hite' ]

for tea, wine, beer in zip(teas, wines, beers): # zip -> eterator를 하나로 묶음
    print(tea, wine, beer)

def wordTrain(*words): # 다중 인수를 사용 할 땐 *를 붙인다. 튜플의 자료형을 가
    for word in words:
        print(word)

    return

wordTrain('개나리', '리어카', '카센터')

def menu(**kwargs): # **를 사용하면 dictionary형태의 인수를 사용가능
    """ 여기는 함수 내의 코멘트를 적는 곳입니다."""
    for when, what in kwargs.items():
        print(when, what)
    return

menus = {
    '점심': '짜장면',
    '저녁': '칼국수',
}

menu(**menus)

menu(lanch='sandwiches', dinner='pasta') #이렇게도 사용가능

"""
여기는 멀티플한 코멘트를 적는 곳 입니다.  
"""

# print(menus.__doc__) # 이렇게 하면 함수내에 존재하는 코멘트만 가져 올 수 있습니다.

# 클로저, 데코레이터
# 클로저는 함수를 리턴하는 함수의 형태입니다.

def calculator(a: int):
    def sum(y: int) -> int:
        return a + y
    return sum

summation = calculator(3)

sum_with_three = summation(2)
print(sum_with_three)

# 데코레이터는 함수의 전, 후처리를 담당하는 함수입니다.
# 함수의 전 후 처리를 한 후에 새로운 함수를 리턴합니다.

def decor(func):
    def decorated(*args, **kwargs):
        print('prev calc')
        new_func = func(*args, **kwargs)
        print('post calc')
        return new_func
    return decorated

@ decor
def printPaper():
    print('A Paper')
    return

printPaper()


# generator

def gen():
    yield 1
    yield 2
    yield 3

num_gen = gen() # 제너레이터 생성

print(next(num_gen))
print(next(num_gen))
print(next(num_gen)) # next 함수의 인자로 호출 될때 마다 제너레이터는 각 yield에 해당하는 값을 출력한다.

# 리스트 내포 표기
tup = (1,2,3,4)

tup_list = [i for i in tup if i % 2 == 0] # 이처럼 표현가능 장점은 메모리를 사용하지 않는다.

print(tup_list)

# 사전 내포 표기

plate = [ 'beef', 'pork', 'chicken' ]
liquor = [ 'wine', 'beer', 'coke' ]

marrige = {x: y for x, y in zip(plate, liquor)}
print(marrige)

# Set도 같은 방법으로 가능
# 제너레이터도 같은 방법으로 가능

# 함수 안에서 전역 변수를 사용하고 싶으면 "global 변수이름" 과 같은 선언을 해주어야 한다.
print(globals()) # 이 스크립트 전체에 대한 정보를 볼 수 있다.

# error handling

try:
    raise Exception
except Exception as ex:
    print(ex)
else:
    print("에러없이 실행되었을 때 여기가 실행됩니다.")
finally:
    print('print whatever happened')

# sorted(iterator, key=(정렬기준 키 혹은 밸류), reverse(boolean))

"""
dic = {}
dic.setdefault() 으로 기본 밸류를 설정할 수 있음
from collections import defaultdict
dic = defaultdict(int) 와 같은 방법도 쓸 수 있음
"""

