"""
**Q4. 입력으로 N각형이 주어졌을 때 대각선이 만나는 점(빨간 점)의 개수를 세는 프로그램을 작성하세요. N각형은 다음 조건을 만족합니다.**

- 대각선 세 개가 한 점에서 만나지 않습니다. (== N각형은 정N각형이 아닙니다.)
- 모든 각이 180도보다 작습니다.
- 3 ≤ N ≤ 30

밑줄은 사용자 입력입니다. 입력을 반복할 필요는 없습니다.

ex )

입력 : 3

출력 : 0

입력 : 4

출력 : 1

입력 : 6

출력 : 15
"""
import math

def get_cross(N):
	# N각형의 대각선의 교차점 개수는 nC4이다.
	if N <= 3:
		print(0)
		return
	crosses = math.factorial(N) / (math.factorial(N-4) * math.factorial(4))
	print(int(crosses))
	return

user_input = int(input("몇각형 입니까?"))

get_cross(user_input)