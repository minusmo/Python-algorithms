# Selection sort 선택 정렬
"""
오름차순, 내림차순으로 배열을 정렬
입력: 배열, 출력: 배열
기존 배열을 변경하지 않으면서 새로운 배열을 리턴.
시간 복잡도: n^2 (베스트/워스트)
공간 복잡도: n (베스트/워스트)
전체 배열중 최소값(최대값) 탐색 -> 새로운 배열에 추가
-> 최소값 제외 배열 중 최소(최대값) 탐색 -> 새로운 배열에 추가
를 반복
"""

unsorted = [ 9, 10, 20, 330, 4, 45, 56, 35, 82, 2, 34, 435 ]

# 2개의 배열을 이용하는 방식
def selection_sort(not_sorted):
	# 빈 배열
	sorted = []
	# 정렬되지 않은 배열
	copied = not_sorted.copy()
	# 숫자개수 - 1 번만큼 반복
	for _ in range(0, len(copied) - 1):
		minimum = min(copied)
		sorted.append(minimum)
		min_index = copied.index(minimum)
		copied.pop(min_index)
	return sorted

print(selection_sort(unsorted))

# 1개의 배열만을 이용하는 방식
def selection_sort_one(not_sorted):
	copied = not_sorted.copy()

	# 숫자개수 - 1 번 만큼 반복
	for i in range(0, len(not_sorted) - 1):
		# 매 첫번째 인덱스를 제외한 나머지 배열에서 최솟값을 찾음
		minimum = min(copied[i:])
		# 찾은 최솟값이 교체하려는 값과 같은 값이면 정렬을 멈춘다
		if not minimum == copied[i]:
			min_index = copied[i:].index(minimum)
			# 최솟값과 첫번째 값을 교환
			copied[i], copied[min_index] = copied[min_index], copied[i]

	return copied


"""
이하는 C언어로 쉽게 풀어쓴 자료구조에서 정리한 것.

선택정렬은 원래 빈 배열과 정렬되지 않은 배열이 있을 때,
오름차순의 정렬에 대하여, 정렬되지 않은 배열에서 가장 작은 값을 선택하여
빈 배열으로 이동하는 정렬 방법이다.
그러나 이 방법은 2개의 배열을 필요로하므로, 메모리를 절약하기 위하여
하나의 배열만을 이용하는 선택 정렬 방법을 고안한다. 

입력 배열에서 최솟값을 발견한 다음,
이를 배열의 첫번재 요소와 교환한다.
다음에는 첫번째 요소를 제외한 나머지 배열에서 최솟값을 발견하고,
이를 두번째 요소와 교환한다. 이 절차를 숫자개수 - 1(배열 길이 - 1)만큼
반복하면 추가적인 배열을 사용하지 않고도 배열이 정렬된다. 
"""