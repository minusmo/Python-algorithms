from math import ceil


a, b, v = input().split()
a, b, v = int(a), int(b), int(v)
print(1 + ceil((v-a)/(a-b)))