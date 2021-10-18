from operator import itemgetter
N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))
members = sorted(members, key=itemgetter(0, 2))
for member in members:
    print(member[0], member[1])