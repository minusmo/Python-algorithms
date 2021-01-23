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

def selection_sort(not_sorted):
	sorted = []
	copied = not_sorted.copy()
	for _ in not_sorted:
		minimum = min(copied)
		sorted.append(minimum)
		min_index = copied.index(minimum)
		copied.pop(min_index)
	return sorted

print(selection_sort(unsorted))