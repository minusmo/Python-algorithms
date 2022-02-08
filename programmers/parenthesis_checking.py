"""
괄호검사.
스택 자료구조 기반.
괄호는 대괄호, 중괄호, 소괄호 총 3가지
조건 1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야한다.
조건 2. 같은 타입의 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야한다.
조건 3. 서로 다른 타입의 왼쪽 괄호와 오른쪽 괄호 쌍은 서로를 교차하면 안된다. (짝이 맞아야한다.)

프로세스:
문자열을 차례대로 검사하다가,
왼쪽 괄호를 만나면 스택에 넣고,
오른쪽 괄호를 만나면 스택에서 가장 최근 왼쪽 괄호를 꺼내어 타입을 맞춰본다.
이 때, 스택이 비어있으면 조건 1,2를 위반하게 되고,
괄호의 짝이 맞지 않으면 조건3에 위배된다.
마지막 괄호까지 검사한 후에도 스택에 괄호가 남아있으면 조건 1에 위배된다.

입력: 문자열
출력: Boolean 값.
"""

def check_parenthesis(str):
	if not type(str).__name__ == 'str':
		print('문자열을 입력해주세요')
		return False

	stack = []
	for char in str:
		if char == '[' or char == '{' or char == '(':
			stack.append(char)
			continue
		elif char == ']' or char == '}' or char == ')':
			if len(stack) == 0:
				print('스택이 비어있습니다.')
				return False
			last_input = stack.pop()
			if not ((last_input == '(' and char == ')') or
			        (last_input == '[' and char == ']') or
			        (last_input == '{' and char == '}')):
				print(last_input, char, '짝이 맞지 않습니다.')
				return False
			else:
				continue

	if not len(stack) == 0:
		print(stack.pop(), '스택이 비어있지 않습니다.')
		return False

	return True

result = check_parenthesis('{ A[(i+1)]=0; }')
print(result)