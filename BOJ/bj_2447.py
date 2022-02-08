N = int(input())

def three_star(n):
    if n == 3:
        return ["***", "* *", "***"]
    else:
        return [i * 3 for i in three_star(n//3)] + [i+' '*(n//3)+i for i in three_star(n//3)] + [i * 3 for i in three_star(n//3)]
    
for i in three_star(N):
    print(i)
    
"""
fblood53 님의 풀이
def star(n):
    if n == 3:
        star_list = ['***', '* *', '***']
        return star_list
    else:
        new_star_list = [x * 3 for x in star(n//3)] + [x + ' '*(n//3) + x for x in star(n//3)] + [x * 3 for x in star(n//3)]
        return new_star_list

for i in star(int(input())):
    print(i)

참고.

재귀 함수 내에서 newline을 출력하면 답이 없다!!!
문자열만 리턴하고 출력은 외부에서 하는 것이 포인트!!!
"""