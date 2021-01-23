"""
Heap sort 힙정렬
제자리 정렬,
시간 복잡도: T = nlogn
Heap(완전 이진 트리)의 구조를 이용한 정렬
최소힙(각 단위 트리의 root 노드가 최소값), 최대힙(각 단위 트리의 root 노드가 최대값)
의 특성을 이용한 정렬
트리를 배열로 치환했을 때의 탐색 방법
i번째 노드의 부모 노드 값: [i/2]
i번째 노드의 왼쪽 자식 노드 값: [2i]
i번째 노드의 오른쪽 자식 노드 값: [2i + 1]
Root 노드로 부터 트리의 높이: logn

Max Heapify (최대힙이 아닌 것을 최대힙으로 만드는 작업)
입력: 배열, 시작 노
시간 복잡도: 힙의 높이 logn * 수행시간 1 == logn
2/n 부터 첫번째 인데스까지 loop 수행

Building a Heap 힙 구조 만들기
수행시간: Max heapify * 수행 횟수(n/2: loop 횟수 * 2: 이진트리) == O(nlogn)

Extract Heap: 트리의 최대값을 뽑아내고 다시 최대힙 구조를 복원하는 것.
root 노드와 가장 마지막 노드의 값을 교체해 최대값을 뽑아내고, 나머지 트리로 최대힙을 복원한다.

1. 배열을 힙 구조로 인식한다.
2. Max(Min) Heapify를 한다.
3. Extract Max(Min)을 반복하며 정렬된 배열을 만든다.
-> root 노드와 마지막 노드를 교체, pop(새로운 배열에 추가), 다시 Max heap 만들기
"""

unsorted = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]

# 배열과 시작 인덱스를 입력으로 받음
def max_heapify(not_sorted, startnode):
	for i in range(startnode, -1, -1):
		print(i)
		try:
			maxi = max(not_sorted[i], not_sorted[2*i + 1], not_sorted[2*i + 2])
		except IndexError:
			try:
				maxi = max(not_sorted[i], not_sorted[2 * i + 1])
			except IndexError:
				print('last node')
				return

		print(maxi)

		if maxi == not_sorted[i]:
			continue
		elif maxi == not_sorted[2*i + 1]:
			not_sorted[2*i + 1] = not_sorted[i]
			not_sorted[i] = maxi
			if not (2*i + 1) >= len(not_sorted):
				max_heapify(not_sorted, 2*i + 1)
		else:
			not_sorted[2*i + 2] = not_sorted[i]
			not_sorted[i] = maxi
			if not (2*i + 2) >= len(not_sorted):
				max_heapify(not_sorted, 2*i + 2)

startindex = (len(unsorted) - 2)//2
max_heapify(unsorted, startindex)
print(unsorted)