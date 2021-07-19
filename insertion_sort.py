# Insertion sort 삽입 정렬
"""
Insertion Sort 삽입정렬
입력: 배열 출력: 오름차순의 배열
기존 배열을 변경하지 않으면서 새로운 배열을 리턴
Best case: 입력 배열이 이미 정렬된 경우 T = 1
Worst case: 입력 배열이 반대로 정렬된 경우 T = n^2
공간복잡도: n

key값(주어진 배열의 첫번째 값)을 정해 새로운 배열에 넣은 후,
그 새로은 배열을 기준으로 기존 배열의 값을 처음부터 비교,
오름차순에 맞는 자리에 값을 insert한다.
비교값보다 작으면 그 값 이전에 삽입(그 자리에 삽입하며 배열의 길이 연장),
비교값보다 크면 계속 비교, 최대값일 경우 마지막에 삽입
"""
# 2개의 배열을 이용하는 방법.
def insertion_sort(not_sorted):
	sorted = []
	copied = not_sorted.copy()
	sorted.append(copied.pop(0))
	for i in range(len(not_sorted) - 1):
		for j in range(len(sorted)):
			if copied[i] > sorted[j]:
				if j == len(sorted) - 1:
					sorted.append(copied[i])
					break
				pass
			else:
				sorted.insert(j, copied[i])
				break
	return sorted


unsorted = [ 9, 10, 20, 330, 4, 45, 56, 35, 82, 2, 34, 435 ]

print(insertion_sort(unsorted))

"""
이하는 C언어로 쉽게 풀어쓴 자료구조에서 정리한 것.
삽입정렬은 정렬되어있는 리스트에 새로운 레코드를 올바른 위치에 삽입하는 과정을 반복한다.
이와 같은 작업을 새로 삽입될 레코드의 수만큼 반복하면 정렬이 완료된다. 
선택정렬의 케이스와 비슷하게 하나의 배열만을 이용해서 정렬을 수행할 수 있다.

삽입정렬은 안정한 정렬방법으로 정렬한 요소의 순서가 유지된다.
"""

# 1개의 배열만 이용하는 방법
def insertion_sort_one(not_sorted):
	copied = not_sorted.copy()

	# 숫자 개수 - 1 번만큼 반복, 시작 인덱스는 1(첫번째 요소는 대상이 아님)
	for i in range(1, len(not_sorted) - 1):
		# target = copied[i]
		target_index = i
		pointing_index = i - 1

		# 좌측 원소부터 타겟이 더 작을때까지만 좌측 원소와 타겟을 교환한다
		while copied[pointing_index] > copied[target_index] and pointing_index >= 0:
			copied[pointing_index], copied[target_index] = copied[target_index], copied[pointing_index]
			pointing_index -= 1
			target_index -= 1

	return copied