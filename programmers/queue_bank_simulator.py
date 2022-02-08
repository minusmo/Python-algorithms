"""
은행 대기열 시스템을 큐로 구성.
하나의 반복 루프로 구성된다.
이 루프 안에서, 먼저 현재 시각을 나타내는 clock이라는
변수를 1증가시키고,
is_customer_arrived 함수를 호출한다.
is_customer_arrived 함수는 난수를 생성하여
시뮬레이션 매개 변수인 arrival_prob와 비교하여
이보다 작으면 새로운 고객이 들어왔다고 판단한다.
만약 is_customer_arrived 함수가 True를 반환하면
insert_customer 함수를 호출한다.
insert_customer는 확률상으로 새로운 고객이 들어올 때가
됐으면 새로운 고객을 위한 데이터(구조체)를 만든다.
데이터: 고객의 아이디, 도착 시간, 서비스 시간 등
그리고 이 구조체를 매개변수로하여 enqueue 함수를 호출한다.
여기서 고객이 필요로하는 서비스 시간은 난수를 이용하여 생성한다.
다음은 지금 서비스하고 있는 고객이 끝났는지를 검사한다.
만약 service_time 이 0이 아니면 아직 어떤 고객이 서비스를 받는 중임을 의미한다.
clock이 하나 증가했으므로 service_time을 하나 감소시킨다.
만약 service_time이 0이면 현재 서비스 받는 고객이 없다.
따라서 큐에서 고객 구조체를 하나 꺼내어 서비스를 시작한다.
(서비스를 시작한다라는 것은 구조체의 service_time을 service_time
변수에 대입하고 시간이 흘러감에 따라 이 service_time을 감소시키는 것이다.)
"""
from random import *

duration = 10
arrival_prob = 0.7
max_serv_time = 5
clock = 0
customers = 0
served_customers = 0
waited_time = 0


def is_customer_arrived():
	global arrival_prob
	arrival = randrange(0, 1)
	if arrival < arrival_prob:
		return True
	else:
		return False

def insert_customer(queue, arrival_time):
	global customers

	new_customer = {
		"id": customers,
		"arrival_time": arrival_time,
		"service_time": randint(0, max_serv_time)
	}
	customers += 1
	queue.append(new_customer)
	print(f"고객 {new_customer['id']}이 {new_customer['arrival_time']}분에 들어옵니다. \n"
	      f"서비스 시간은 {new_customer['service_time']}분입니다.")

def remove_customer(queue):
	if len(queue) == 0:
		return 0
	customer = queue.pop(0)
	service_time = customer['service_time'] - 1
	global served_customers, waited_time, clock
	served_customers += 1
	waited_time += clock - customer['arrival_time']
	print(f"고객 {customer['id']}이 {clock}분에 서비스를 시작합니다.\n"
	      f"대기시간은 {clock - customer['arrival_time']}이었습니다.")
	return service_time

def print_stat():
	global served_customers, waited_time, customers
	print(f"서비스 받은 고객수: {served_customers}")
	print(f"전체 대기 시간: {waited_time}분")
	print(f"1인당 평균 대기 시간: {waited_time/served_customers}")
	print(f"아직 대기중인 고객수: {customers - served_customers}")


def simulate():
	global clock, duration
	service_time = 0
	queue = []
	while clock < duration:
		clock += 1
		print(f"현재시각: {clock}")
		if is_customer_arrived():
			insert_customer(queue, clock)
		if service_time > 0:
			service_time -= 1
		else:
			service_time = remove_customer(queue)
	print_stat()

simulate()
