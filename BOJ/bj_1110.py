N = int(input())

origin = N
cycle = 1

def make_new(n):
    n = str(n)
    if len(n) == 2:
        new = (int(n[0])+int(n[1]))%10 + int(n[1])*10
        return new
    else:
        new = int(n) + int(n)*10
        return new

new = make_new(N)
while not origin == new:
    new = make_new(new)
    cycle += 1
print(cycle)