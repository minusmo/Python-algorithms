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

