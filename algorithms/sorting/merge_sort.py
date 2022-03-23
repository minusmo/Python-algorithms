"""
Merge Sort 병합(합병)정렬
입력: 2개의 정렬되어있는 배열
출력: 1개의 정렬되어있는 배열

Divde and Conquer 접근
-> 원래 합병정렬은 입력이 2개의 정렬된 배열이기 때문에
하나의 정렬되지 않은 배열을 입력으로 받았을 때, 정렬된 하나의 배열을 리턴하기 위함
시간복잡도: nlogn (최악, 평균, 최선의 3가지 경우)
합병정렬은 안정된 정렬방법

합병정렬읜 단점.
1. 임시배열이 필요하다.
2. 레코드들의 크기가 큰 경우에는 이동횟수가 많으므로 매우 큰 시간적낭비를 초래한다.
그러나 레코드를 연결리스트를 이용하여 구성하여 정렬할 경우, 링크 인덱스만 변경하면 되므로
데이터의 이동은 무시할 수 있을 정도로 작아진다. 따라서 크기가 큰 레코드를 정렬할 경우,
연결 리스트를 이용하면 굉장히 효율적인 정렬 방법이 될 수 있다.

재귀함수에서 중요한 것
1. 종결조건: 최소 단위를 리턴한다.
2. 일종의 프랙탈 형태로, 함수가 가장 작은 작업 단위와 가장 큰 작업 단위의 형태가 같다.
-> 가장 단순한 형태(가장 작은 단위)를 생각한다.
"""


unsorted = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]

def merge_sort(not_sorted):
	# 두개의 정렬된 배열을 받아 하나의 정렬된 배열을 리턴하는 함수를 정의한다.
	def merge(sorted_1, sorted_2):
		sortedlist = []
		while len(sorted_1) != 0 and len(sorted_2) != 0:
			if sorted_1[0] <= sorted_2[0]:
				sortedlist.append(sorted_1.pop(0))
			else:
				sortedlist.append(sorted_2.pop(0))
		sortedlist = sortedlist + sorted_1 + sorted_2
		return  sortedlist

	# 종결 조건: 입력 배열이 1개이면 그 배열을 리턴한다.
	# 배열을 나누는 작업의 최종 단계, 출력을 정해주는것!!
	if len(not_sorted) == 1:
		return not_sorted

	# 재귀를 이용해서 작업을 divide한다.
	# 위의 종결조건으로 인해 최소 작업 단위의 출력값을 할당할 수 있다.
	sorted1 = merge_sort(not_sorted[0:len(not_sorted)//2])
	sorted2 = merge_sort(not_sorted[len(not_sorted)//2:])

	# 정렬된 두 배열을 하나의 정렬된 배열로 만들어 리턴한다.
	return merge(sorted1, sorted2)

print(merge_sort(unsorted))