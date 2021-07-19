"""
Quick Sort 퀵정렬

Divde and Conquer 접근 사용
pivot을 정해 그것을 기준으로 좌우(더 작은 것과 큰 )로 분류,
이후 recursive하게 배열을 절반씩 나누어
정렬하는 방법
Best Case: nlogn balanced partition
Worst Case: n**2 unbalanced partition

Worst case를 방지하기 위해 pivot을
Random하게 선택하는 Randomized Quick sort를 실행한다.
"""
import random

def quick_sort(not_sorted):
	sorted = []

	if len(not_sorted) == 1:
		return not_sorted.copy()
	# 랜덤으로 pivot index를 결정한다.
	try:
		randomP = random.randint(0, len(not_sorted) - 1)
	except ValueError:
		return not_sorted.copy()
	# except RecursionError:
	# 	print(not_sorted)
	# 	return not_sorted.copy()

	sorted.append(not_sorted[randomP])

	pointer = 0
	for i in not_sorted:
		if i == not_sorted[randomP]:
			continue
		if i >= sorted[pointer]:
			sorted.append(i)
		else:
			sorted.insert(pointer, i)
			pointer += 1

	# pivot 좌우를 다시 sorting 하는 것이기 때문에 pivot은 포함하지 않는다.
	left_sorted = quick_sort(sorted[0:pointer])
	right_sorted = quick_sort(sorted[pointer + 1:])

	return left_sorted + [sorted[pointer]] + right_sorted

unsorted = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]

print(quick_sort(unsorted))

"""
이하 C언어로 풀어쓴 자료구조에 따른 퀵소트 방법,
재귀와 partition함수를 이용한 방법으로
재구성할 필요가 있음. 
"""

def quick_sort_one(unsorted, left, right):
	if left < right:
		q = partition(unsorted, left, right)
		quick_sort_one(unsorted, left, q - 1)
		quick_sort_one(unsorted, q + 1, right)

def partition(unsorted, left, right):
	low = left
	high = right
	pivot = unsorted[left]

	# C언어에서는 do while loop를 사용한다.
	# python에서는 do while loop를 지원하지 않으므로, while loop를 응용하여 사용한다.
	while True:
		while True:
			low += 1
			if low > right or unsorted[low] >= pivot:
				break

		while True:
			high -= 1
			if high < left or unsorted[low] <= pivot:
				break

		if low < high:
			unsorted[low], unsorted[high] = unsorted[high], unsorted[low]

		if low >= high:
			break

	unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
	return high


