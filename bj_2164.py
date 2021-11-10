from queue import SimpleQueue
sq = SimpleQueue()
cards = int(input())
for i in range(0, cards):
    sq.put(i+1)
do = True

if  sq.qsize() == 1:
    print(sq.get())
else:
    while not sq.qsize() == 1:
       if do:
            sq.get()
            do = not do
       else:
           sq.put(sq.get())
           do = not do
    print(sq.get())