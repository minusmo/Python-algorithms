word = input()
def dial_time(char):
    if 65 <= ord(char) <= 67:
        return 3
    elif 68 <= ord(char) <= 70:
        return 4
    elif 71 <= ord(char) <= 73:
        return 5
    elif 74 <= ord(char) <= 76:
        return 6
    elif 77 <= ord(char) <= 79:
        return 7
    elif 80 <= ord(char) <= 83:
        return 8
    elif 84 <= ord(char) <= 86:
        return 9
    else:
        return 10
    
call_time = 0
for char in word:
    call_time += dial_time(char)
    
print(call_time)