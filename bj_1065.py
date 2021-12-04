N = int(input())

h = 0

def hanSu(n):
    if len(str(n)) <= 2:
        return True
    
    diff = 0
    for i in range(len(str(n))):
        try:
            next_diff = int(str(n)[i+2])-int(str(n)[i+1])
            diff = int(str(n)[i+1])-int(str(n)[i])
            if diff != next_diff:
                return False
        except:
            break
    return True
        
for i in range(1,N+1):
    if hanSu(i):
        h += 1
        
print(h)