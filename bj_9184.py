def w(a,b,c):
    if a <= 0 and b <= 0 and c <= 0:
        return 1
    elif a > 20 and b > 20 and c > 20:
        a, b, c = 20, 20, 20
    
    last_index_of_ws = max(a,b,c)*6
    ws = [-1]*(last_index_of_ws+1)
    ws[0] = 1
    ws[1], ws[2], ws[3], ws[4], ws[5], ws[6], ws[7] = 1, 1, 1, 1, 1, 1, 1
    # wa = [-1]*(last_index_of_ws+1)
    # wb = [-1]*(last_index_of_ws+1)
    # wc = [-1]*(last_index_of_ws+1)
    # wa[0], wb[0], wc[0] = 1, 1, 1
    
    for i in range(8,last_index_of_ws+1):
        # from index 8, which is w(1,1,1) 8%7==1
        if i%7 == 3 or i%7 == 6:
            # 001 011
            ws[i] = ws[i]