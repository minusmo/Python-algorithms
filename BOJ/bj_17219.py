N, M = map(int, input().split())

add_pass = {}
for _ in range(N):
    addpass = input().split()
    add_pass[addpass[0]] = addpass[1]
for _ in range(M):
    address = input()
    print(add_pass[address])