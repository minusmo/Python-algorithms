while 1:
    palind = input()
    if int(palind) == 0:
        break
    original = palind
    palind = list(palind)
    palind.reverse()
    reversed = "".join(palind)
    if original == reversed:
        print('yes')
    else:
        print('no')