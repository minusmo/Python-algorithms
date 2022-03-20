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

from queue import Queue

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

"""
이하는 C언어로 쉽게 풀어쓴 자료구조에서 정리한 것.
기수 정렬은 레코드들을 비교하지 않고도 정렬하는 방법.
기존의 비교를 통한 정렬 방법은 이론적인 하한선인 O(nlog2n)을 깰 수 없는데,
기수 정렬은 이 하한선을 깰 수 있는 유일한 기법이다. 

기수 정렬은 O(dn)의 시간 복잡도를 가지는 데, 대부분 d < 10 이하이다.
문제는 기수정렬은 추가적인 메모리 공간을 필요로 하는데, 이를 감안하더라도
기수정렬은 다른 대부분의 정렬 방법보다 상당히 빠르다. 

기수정렬의 단점은, 정렬하려는 레코드들의 타입이 한정된다는 점이다. 
즉, 기수정렬을 사용하려면 레코드들의 키들이 동일한 길이를 가지는 숫자나 문자열로 구성되어야한다.

기수(Radix)란 숫자의 자릿수이다. 예를 들면 42는 4와 2 두개의 자릿수를 가지고, 이것이 기수가 된다.
기수 정렬은 다단계 정렬이다. 단계의 수는 데이터의 자릿수의 개수와 일치한다. 

기수 정렬은 버켓(추가 메모리 배열)을 사용하여 크기 순으로 순서가 정해진 버켓에다
정렬되지않은 배열의 숫자들을 투입하고, 이를 정렬된 배열로 다시 출력한다.

자릿수가 많은 숫자들의 배열의 경우에는 낮은 자리의 숫자를 기준으로 먼저 기수정렬을 하고,
그 다음 큰 자리의 숫자들로 기수정렬을 하는 방식으로 기수 정렬을 한다. 

버켓의 숫자(배열 길이)는 진법(2, 10 등등)과 일치한다.
ex) 만약 알파벳이라면 26개의 버켓이 필요할 것이다. 

버켓은 일종의 우선순위 큐의 자료구조를 가진다.
그 이유는 먼저 들어간(우선 순위가 낮은 것, 자릿수가 작은 것) 순서대로 나와야하기 때문이다.  

아래는 본문에 나와있는 기수정렬 함수를 구현한 것이다.

python에서는 Queue 클래스를 제공하므로 이를 이용해 큐를 생성한다.
(기본 list 클래스를 이용하는 것보다 성능이 좋다.)
"""
DIGITS = 3 # 자릿수
BUCKETS = 10 # 각 버켓은 큐로 구성된다.

def radix_sort_one(unsorted, n):
	global DIGITS
	global BUCKETS
	factor = 10 # 진법(단위)
	# 큐(각 버켓)를 초기화한다.
	queues = [Queue() for _ in range(BUCKETS)]

	for d in range(0, DIGITS):
		for i in range(0, n):
			# queues[(unsorted[i]/factor)%10].append(unsorted[i])
			queues[(unsorted[i]/factor)%10].put(unsorted[i])
		j = 0
		for b in range(0, BUCKETS):
			while not queues[b].empty():
				j += 1
				unsorted[j] = queues[b].get()
		factor *= 10