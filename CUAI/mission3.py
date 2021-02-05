"""
**Q3. 다음 조건을 만족하는 함수를 define 하세요.**

- 함수 이름은 maxAvg()이며, 사용자가 입력한 실수들의 최댓값과 평균을 반환합니다.
- 사용자는 2개 이상 5개 이하의 실수들을 입력합니다.

밑줄은 사용자 입력입니다.

ex)

입력을 멈추고 싶으면 음수를 입력하세요.

숫자를 입력하십시오: 63.4

숫자를 입력하십시오: 319.6

숫자를 입력하십시오: 815.5

숫자를 입력하십시오: -3

입력한 숫자들의 최댓값: 815.5

입력한 숫자들의 평균값: 399.5
"""

def maxAvg(floats):
	print("입력한 숫자들의 최댓값:", max(floats))
	print("입력한 숫자들의 평균값:", sum(floats)/len(floats))

print("입력을 멈추고 싶으면 음수를 입력하세요")

numbers = []

while 1:
	user_input = float(input("숫자를 입력하십시오:"))

	if user_input < 0:
		break

	numbers.append(user_input)

maxAvg(numbers)