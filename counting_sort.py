"""
Counting Sort 계수 정렬
배열의 원소가 각 몇개 씩인지를 세어
오름차순으로 정렬하는 방법
입력: 배열 1개
출력: 정렬된 배열 1개

원본 배열을 수정하지 않는 함수
"""

def counting_sort(not_sorted):
	maxi = max(not_sorted)
	sorted = []

	# 배열의 쵀대값을 최대 인덱스로 가지는 배열을 만든다.
	# 그 배열의 인덱스를 iterate하며 원본 배열에 각 인덱스가 몇개인지 count한다.
	for i in range(0, maxi + 1):
		sorted.append(not_sorted.count(i))

	# count한 배열의 각 인덱스까지의 value를 처음부터 누산한 값을 value로 가지는 배열을
	# 만든다. -> 정렬된 배열에서의 정확한 인덱스를 얻기 위해.
	cum_sorted = []
	for i in range(0, maxi + 1):
		if i == maxi:
			cum_sorted.append(sum(sorted[0:]))
			break
		cum_sorted.append(sum(sorted[0:i+1]))

	count_sorted = [0] * (len(not_sorted))

	# 원본 배열을 iterate하여 각 value의 인덱스를 찾아
	# 정렬된 배열의 해당 인덱스에 원본 배열의 값을 넣는다.
	for i in not_sorted:
		count_sorted[cum_sorted[i] - 1] = i
		# 중복되는 숫자를 처리하기 위해 포인터를 옮기는 개념
		cum_sorted[i] -= 1

	return count_sorted


unsorted = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22, 22 ]

print(counting_sort(unsorted))