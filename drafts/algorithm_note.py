# a, b, c = input().split()
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# min = (a if a<=b else b) if ((a if a<=b else b)<=c) else c
#
# print(min)

# filterd = list(filter(lambda x: len(x) > 1, text.split("\n")))
# joined = " ".join(filterd)
# print(filterd, len(filterd), sep="\n")
# print(joined)
#
# import datetime
#
# print(datetime.datetime.now().date())

# u = input()
# a = int(u, 16) # 16진수를 정수로 변환
# b = a * int('A', 16) # 16진수를 정수로 변환한 후 곱 연산.
# d = b//16
# r = b%16
# result = hex(d)[-1] + hex(r)[-1]
# print(a, b, hex(d), hex(r), result)

# 1부터 15까지를 16진수로 변환
# 10이상 부터는 15까지 알파벳으로 맵핑


# u = input()
# a = int(u, 16)
# for i in range(1, 16):
# 	h = hex(i)[-1]
# 	b = a * int(h, 16)
# 	d = b // 16
# 	r = b % 16
# 	if i == 1:
# 		res = hex(r)[-1].capitalize()
# 	else:
# 		res = hex(d)[-1].capitalize() + hex(r)[-1].capitalize()
# 	print(u,"*", h.capitalize(), "=",res, sep="")
#
# "1".capitalize()

# r, g, b = input().split()
#
# ms = int(r) * int(g) * int(b)
#
# for i in range(0, int(r)):
# 	for j in range(0, int(g)):
# 		for k in range(0, int(b)):
# 			print(i, j, k, sep=" ")
#
# print(ms)

# h,b,c,s = input().split()
#
# byte = int(h) * int(b) * int(c) * int(s)
#
# mb = byte / 8 / 2**10 / 2**10
#
# print(f"{mb:.1f} MB")

# w, h, b = input().split()
#
# size = int(w) * int(h) * int(b) / 8 / 2**10 / 2**10
#
# print(f"{size:.2f} MB")

# n = int(input())
# nums = input().split()
#
# nums = [int(num) for num in nums]
#
# p = [0 for _ in range(23)]
#
# for j in nums:
# 	p[j-1] += 1
#
# for per in p:
# 	print(per, end=" ")

# a = int(input())
# n = input().split()
# min = 1000
# for i in range(a):
# 	if int(n[i]) <= min:
# 		min = int(n[i])
# print(min)

# d = [[0 for _ in range(19)] for _ in  range(19)]
#
# n = int(input())
# for i in range(n):
# 	x, y = input().split()
# 	d[int(x)-1][int(y)-1] = 1
#
# for i in range(19):
# 	for j in range(19):
# 		print(d[i][j], end=" ")
# 	print()

# l = []
# for _ in range(19):
# 	d = input().split()
# 	l.append(d)
#
# n = int(input())
#
# for i in range(n):
# 	col, row = input().split()
# 	for j in range(19):
# 		if l[j][int(col)-1] == '0':
# 			l[j][int(col)-1] = '1'
# 		else:
# 			l[j][int(col)-1] = '0'
#
# 		if l[int(row)-1][j] == '0':
# 			l[int(row)-1][j] = '1'
# 		else:
# 			l[int(row)-1][j] = '0'
#
# for i in range(19):
# 	for j in range(19):
# 		print(l[i][j], end=" ")
# 	print()

# h, w = input().split()
# n = int(input())
#
# table = [[0 for _ in range(int(w))] for _ in range(int(h))]
#
# for _ in range(n):
# 	m, direction, x, y = input().split()
# 	if direction == '0':
# 		for i in range(int(m)):
# 			table[int(x)-1][int(y)-1+i] = 1
# 	else:
# 		for i in range(int(m)):
# 			table[int(x)-1+i][int(y)-1] = 1
#
# for row in table:
# 	for col in row:
# 		print(col, end=" ")
# 	print()

# print('\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \(__)|')
# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\__|')

# a, b = input().split()

# a = int(input())
#
# for i in range(1, 10):
# 	print(f"{a} * {i} = {a * i}")

# hh, mm = input().split()
# hh = int(hh)
# mm = int(mm)
# if hh == 0:
# 	tot = 24 * 60 + mm - 45
# 	if mm <= 59 and mm >= 45:
# 		print(0, tot % 60, sep=" ")
# 	else:
# 		print(tot // 60, tot % 60, sep=" ")
# else:
# 	tot = hh * 60 + mm - 45
# 	print(tot // 60, tot % 60, sep=" ")
# H = tot // 60
# M = tot % 60
# print(tot // 60, tot % 60, sep=" ")

# t = int(input())
#
# for _ in range(t):
# 	a, b = input().split()
# 	print(int(a) + int(b))
#
# a = input().split()
# print(len(a))

# max = 0
# max_index = 0
# for i in range(1, 10):
# 	a = int(input())
# 	if a > max:
# 		max = a
# 		max_index = i
#
# print(max, max_index, sep="\n")
#
# a = int(input())
# b = int(input())
# c = int(input())

# mul = a * b * c
# counts = [0 for _ in range(0, 10)]
#
# for char in str(mul):
# 	if char == "0":
# 		counts[0] += 1
# 	elif char == "1":
# 		counts[1] += 1
# 	elif char == "2":
# 		counts[2] += 1
# 	elif char == '3':
# 		counts[3] += 1
# 	elif char == '4':
# 		counts[4] += 1
# 	elif char == '5':
# 		counts[5] += 1
# 	elif char == '6':
# 		counts[6] += 1
# 	elif char == '7':
# 		counts[7] += 1
# 	elif char == '8':
# 		counts[8] += 1
# 	else:
# 		counts[9] += 1
#
# for num in counts:
# 	print(num)

# T = int(input())
# for _ in range(T):
#
# 	R, S = input().split()
#
# 	P = ""
#
# 	for char in S:
# 		P += char * int(R)
#
# 	print(P)

# a, b = input().split()
#
# Ra = ''
# Rb = ''
#
# for i in range(len(a)-1, -1, -1):
# 	Ra += a[i]
# Ra = int(Ra)
#
# for j in range(len(b)-1, -1, -1):
# 	Rb += b[j]
# Rb = int(Rb)
#
# print(max(Ra, Rb))

# a = input().split(' ')
# a = [int(i) for i in a]

# isAsc = True
# isDesc = True
# isMix = True

# for i in range(1, 9):
# 	if a[i-1] != i:
# 		isAsc = False

# for i in range(8, 0, -1):
# 	if a[8-i] != i:
# 		isDesc = False

# if isDesc or isAsc:
# 	isMix = False

# if isAsc:
# 	print('ascending')
# if isDesc:
# 	print('descending')
# if isMix:
# 	print('mixed')

# n = []

# for _ in range(10):
# 	n.append(int(input()))
 
# n = [int(i) for i in n]

# n = [i % 42 for i in n] 

# n = set(n)

# print(len(n))

# T = int(input())

# for _ in range(T):
#     a = input()
#     acc = 0
#     sum = 0
#     for i in a:
#         if i == 'O':
#            acc += 1
#            sum += acc
#         else:
#             acc = 0
#     print(sum)

# s = input()
# alphab = [None for _ in range(26)]
# for i in range(97, 123):
# 	ind = s.find(chr(i))
# 	alphab[i - 97] = ind
# for c in alphab:
#     print(c, end=" ")

# N = int(input())

# M = input().split(' ')
# M = [int(i) for i in M]
# L = [(j / max(M)) * 100 for j in M]

# print(sum(L)/N)

# s = input()
# s = s.lower()
# d = dict()

# for char in s:
#     if char in d:
#         d[char] += 1
#     else:
#         d[char] = 0

# maxKey = ""
# maxVal = -1
# for key, val in d.items():
#     if int(val) > maxVal:
#         maxVal = val
#         maxKey = key
#     elif int(val) == maxVal:
#         maxKey = "?"
#         continue
# print(maxKey.upper())

# x, y, w, h = input().split()
# x = int(x)
# y = int(y)
# w = int(w)
# h = int(h)

# minx = min(w - x, x)
# miny = min(h - y, y)
# print(min(minx, miny))

# while True:
#     a, b, c = input().split()
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     if a == 0 and b == 0 and c == 0:
#         break
#     maxi = max(a,b,c)
#     if (a**2 + b**2 + c**2 - maxi**2) == maxi**2:
#         print('right')
#     else:
#         print('wrong')

# T = int(input())

# for _ in range(T):
#     h, w, n = input().split()
#     h, w, n = int(h), int(w), int(n)
#     wind = (n-1) // h + 1
#     hind = n % h
#     if hind == 0:
#         hind = h
#     room_number = hind * 100 + wind
#     print(room_number)

N = int(input())
Ms = []
for i in range(1, N+1):
    m = i
    for j in str(i):
        m += int(j)
    if m == N:
        Ms.append(i)
if len(Ms) == 0:
    print(0)
else:
    print(min(Ms))