"""
Radix Sort 기수 정렬
입력: 비정렬 배열
출력: 정렬 배열

Counting Sort의 응용.
각 자리수마다 Counting Sort를 실행
배열의 숫자를 1의 자리부터 오름차순으로 정렬하는 방법.
1의자리 부터 오름차순으로 정렬
-> 10의 자리로 오름 차순으로 정렬
-> 100의 자리로 오름 차순으로 정렬

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
		cum_sorted[i] -= 1

	return count_sorted

def radix_sort(not_sorted):
	maxi = max(not_sorted)
	copied = not_sorted.copy()
	times = 0

	print(maxi)
	while maxi // 10 != 0:
		maxi = maxi // 10
		times += 1

	print(times)
	counts = []
	for i in range(times, -1, -1):
		counts.append([j // 10**i for j in copied])
		copied = [j % 10**i for j in copied]

	print(counts)
	for i in range(0, times + 1):
		counts[i] = counting_sort(counts[i])

	print(counts)
	radix_sorted = []
	for i in range(0, len(not_sorted)):
		sum = 0
		for j in range(0, len(counts)):
			sum += counts[j][i]
		radix_sorted.append(sum)

	return radix_sorted

unsorted = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]

print(radix_sort(unsorted))
