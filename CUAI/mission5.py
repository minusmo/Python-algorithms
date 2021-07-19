"""
**Q5. 정렬 알고리즘을 사용하여 지원자들의 번호대로 이름을 출력하는 프로그램을 만드세요.**

면접관 나혁이는 CUAI 면접 순서에 맞게 지원자들의 줄을 세우려고 합니다. 이미 부여된 면접 번호대로 사람들의 줄을 세울 예정입니다.
 면접 순서가 적힌 쪽지에는 다음과 같이 적혀 있습니다.

- 1번 Jerry, 2번 Mike, 3번 Tom, 4번 Rachel, 5번 Jackson

정렬 알고리즘을 사용하여 지원자들의 번호대로 이름을 출력하는 프로그램을 만드세요. 첫째 줄에는 지원자들의 수 N, 둘째 줄부터는
지원자들의 이름과 면접 순서가 입력됩니다.

밑줄은 사용자 입력입니다.

ex)

입력 :

5

Mike 2

Rachel 4

Jerry 1

Jackson 5

Tom 3

출력 :  Jerry Mike Tom Rachel Jackson

시간복잡도: O(n)
이미 인덱스가 정해져 있으므로 정렬의 필요가 없다.
입력하는데 필요한 시간이 입력의 개수에 비례할 뿐이다.
"""

applicants = int(input())

app_list = [None] * applicants

for _ in range(0, applicants):
	applicant = input()
	app_list[int(applicant[-1]) - 1] = applicant[-1*len(applicant):-2]


for name in app_list:
	print(name, end=" ")
