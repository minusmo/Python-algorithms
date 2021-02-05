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