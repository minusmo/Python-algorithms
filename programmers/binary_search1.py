def solution(n, times):
    people_waiting = n
    people_examining = len(times)
    min_examine_time = get_min_examine_time(people_waiting, people_examining, times)
    return min_examine_time

def get_min_examine_time(people_waiting, number_of_people_examining, people_examining):
    min_time = 1
    max_time = people_waiting * max(people_examining)
    examine_time = 0
    while min_time <= max_time:
        middle_time = (min_time + max_time) // 2
        people_examined = determine_available(people_waiting, people_examining, middle_time)
        if people_examined >= people_waiting:
            examine_time = middle_time
            max_time = middle_time - 1
        else:
            min_time = middle_time + 1
    return examine_time

def determine_available(people_waiting, people_examining, middle_time):
    people_examined = 0
    for examine_time in people_examining:
        people_examined += middle_time // examine_time
        if people_examined >= people_waiting:
            break
    return people_examined

"""
https://hyoeun-log.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89-%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%A0%81%EC%9A%A9%ED%95%A0-%EA%B2%83%EC%9D%B8%EA%B0%80?category=848128
위의 풀이 참조.

매개변수 탐색을 이용.
주어진 매개변수에 대해 가능한지를 판별하는 알고리즘을 적절히 알아내는 것이 핵심.
"""