def solution(N):
    B = bin(N).replace('0b','')
    K = str(B)
    K = list(K)
    Max = 0
    C = 0
    S = 0
    Flag = False
    for i in range(len(K)):
        if K[i] is '1' and C is 0 and Flag is False:
            C=i
            Flag = True
        elif K[i] is '1' and Flag:
            S=i
            if Max<abs(S-C):
                Max = abs(S-C)
                C=S
            Flag = False
    if ((Max-1) < 0):
        res = 0
    else:
        res = Max-1
    return res