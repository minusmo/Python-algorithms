from queue import deque
N = int(input())

class Stack:
    def __init__(self):
        self._st = deque()
        self._count = 0
        self._topidx = -1
        
    def push(self,num):
        self._st.append(num)
        self._count += 1
        self._topidx += 1
        
    def pop(self):
        if self._count == 0:
            print(-1)
            return
        self._count -= 1
        self._topidx -= 1
        print(self._st.pop())
        
    def size(self):
        print(self._count)
        
    def empty(self):
        if self._count == 0:
            print(1)
        else:
            print(0)
            
    def top(self):
        if self._count == 0:
            print(-1)
            return
        num = self._st.pop()
        print(num)
        self._st.append(num)
        
commands = deque()
for _ in range(N):
    commands.append(input())
    
st = Stack()
nums = set([str(i) for i in range(10)])
for command in commands:
    command.strip()
    if command[-1] in nums:
        com, inp = command.split()
        if com == "push":
            st.push(inp)
        elif com == "top":
            st.top()
        elif com == "size":
            st.size()
        elif com == "empty":
            st.empty()
        elif com == "pop":
            st.pop()
    else:
        if command == "push":
            st.push(inp)
        elif command == "top":
            st.top()
        elif command == "size":
            st.size()
        elif command == "empty":
            st.empty()
        elif command == "pop":
            st.pop()
            
# 리스트는 너무 느리다. deque을 적극 활용하자
# 역시 리스트는 느리다. set, dict를 적극 활용하자