"""
수식의 계산
수식을 표기하는 방법은 전위, 중위, 후위가 있다.
그중 컴퓨터는 후위 표기법으로 계산을 한다.
(정확히는 컴파일러가) 인간이 중위 표기법으로 입력을 하면,
컴파일러는 이를 후위로 바꾼후에 스택을 사용하여 계산한다.
(후위표기법은 괄호가 필요없기 때문에)

스택을 사용하여 수식을 계산하는 법.
수식을 차례대로 검사하여,
피연산자이면 스택에 추가하고,
연산자이면 필요한 수만큼의 피연산자를 스택에서 꺼내 연산을 실행하고
연산의 결과를 다시 스택에 저장한다.

중위표기법을 후위표기법을 바꾸는 방법.
(스택은 괄호와 연산자의 저장에만 사용한다.)
중위표기법과 후위표기법은 피연산자의 순서는 같지만 연산자의 순서가 다르다.(연산자의 우선순위에 따라 결정)
기본적으로는 후입선출의 순서를 사용.(연산자를 스택에 저장)
그러나 연산자간의 순서가 분명하므로,
연산자를 스택에 저장할 때는 저장된 연산자의 우선순위가 저장할 연산자의 우선순위보다
높으면, 우선순위가 높은 연산자를 꺼내서 출력하고, 우선순위가 낮은 연산자를 저장 해야한다.
우선순위가 같은 경우에도 일단 스택 상단의 요소를 꺼내어 출력한다.
(스택에 저장된 연산자와 저장할 연산자를 비교하여, 저장할 연산자의 우선순위가
저장된 연산자의 우선순위보다 높을 경우에만 스택에 저장한다.)

괄호의 처리방법.
왼쪽 괄호는 무조건 스택에 삽입한다.
왼쪽 괄호가 일단 스택에 삽입되면, 이 괄호를 가장 우선순위가 낮은 연산자로 취급한다.
(즉, 이 다음에 나오는 어떤 연산자도 스택에 넣는다.)
그러다 오른쪽 괄호를 만나면, 왼쪽 괄호가 삭제될 때까지 왼쪽 괄호 위의 모든 연산자들을 출력한다.
"""
parenthesis = ['(', '[', '{', ')', ']', '}']
left_parenthesis = parenthesis[0:3]
right_parenthesis = parenthesis[3:]
operators = ['+', '-', '*', '/']

def get_priority(operator):
	if operator in parenthesis:
		return 0
	elif operator == '+' or operator == '-':
		return 1
	elif operator == '*' or operator == '/':
		return 2
	else:
		return -1

def mid_to_post(str):
	if not type(str).__name__ == 'str':
		print('문자열을 입력해주세요')
		return False
	stack = []
	post_fix = ""
	for char in str:
		if char in left_parenthesis:
			print(char)
			stack.append(char)
		elif char in right_parenthesis:
			print(char)
			top_element = stack.pop()
			if char == ')':
				while not top_element == '(':
					post_fix += top_element
					top_element = stack.pop()
			elif char == ']':
				while not top_element == '[':
					post_fix += top_element
					top_element = stack.pop()
			else:
				while not top_element == '{':
					post_fix += top_element
					top_element = stack.pop()
		elif char in operators:
			print(char)
			try:
				top_element = stack[-1]
			except:
				print('stack is empty')
				stack.append(char)
				continue
			top_priority = get_priority(top_element)
			if get_priority(char) > top_priority:
				print(char)
				stack.append(char)
			else:
				top_element = stack.pop()
				while not (get_priority(top_element) == 0):
					post_fix += top_element
					try:
						top_element = stack.pop()
					except:
						print('stack is empty')
						break
				stack.append(char)
		else:
			print(char)
			post_fix += char
	print(stack)
	for op in stack:
		post_fix += op
	return post_fix



def calc_post(post):
	stack = []
	for char in post:
		if not char in operators:
			stack.append(char)
		else:
			second = stack.pop()
			first = stack.pop()
			result = None
			if char == '+':
				result = int(first) + int(second)
			elif char == '-':
				result = int(first) - int(second)
			elif char == '*':
				result = int(first) * int(second)
			else:
				result = int(first) / int(second)
			stack.append(result)
	print(stack)
	return stack.pop()

test_1 = '(1+2)*3'
test_2 = '(1+2*3)*4'

post_fix1 = mid_to_post(test_1)
print(post_fix1)
result_1 = calc_post(post_fix1)
print(result_1)

post_fix2 = mid_to_post(test_2)
print(post_fix2)
result_2 = calc_post(post_fix2)
print(result_2)
