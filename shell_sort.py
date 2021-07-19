"""
Shell sort(셸 정렬)
도널드 셸이 제안한 방법으로, 삽입 정렬이 어느정도 정렬된 배열에 대해서는
대단히 빠르다는 것에 착안한 방법이다. 이는 삽입 정렬 O(n^2)보다 빠르다.
평균적인 경우에 대하여 셸정렬은 O(n^1.5)의 시간 복잡도를 보인다.

삽입 정렬의 문제점은 요소들이 삽입될 때, 이웃한 위치로만 이동한다는 것이다.
만약 삽입되어야할 위치가 현재 위치에서 먼 곳이라면, 상당히 많은 이동이 필요하다.
셸 정렬에서는 요소들이 멀리 떨어진 위치로도 이동할 수 있다.

부분 리스트를 구성할 때는 주어진 리스트의 각 k번째 요소를 추출하여 만든다.
이 k를 간격(gap)이라고 한다.
각 스텝마다 간격 k를 줄여가므로 수행 과정이 반복될 때마다 하나의 부분 리스트에 속하는 레코드들의 개수는 증가한다.
마지막 스텝에서의 간격은 1이 된다.

간격은 처음에는 n/2로하고, 각 패스마다 절반으로 줄이는 방식을 사용한다.
"""

# gap 만큼 떨어진 요소들을 삽입정렬
# 정렬의 범위는 first에서 last

def inc_insertion_sort(unsorted, first, last, gap):
	for i in range(first+gap, last+1, gap):
		key = unsorted[i]
		for j in range(i - gap, first - 1, -1 * gap):
			if key >= unsorted[j]:
				break
			unsorted[j+gap] = unsorted[j]
		unsorted[j+gap] = key

def shell_sort(unsorted, size):
	step = size / 2
	for gap in range(size / 2, 0, step):
		if gap % 2 == 0:
			gap += 1
		for i in range(0, gap, 1):
			inc_insertion_sort(unsorted, i, size - 1, gap)

		step = step / 2
