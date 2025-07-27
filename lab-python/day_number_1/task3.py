N, M, K, Ta, Tb, Tc = map(float, input().split())

stairs = abs(M - N) * Tc
elevator = abs(K - N) * Ta + 3 * Tb + abs(M - N) * Ta
if stairs < elevator:
    print('stairs')
else:
    print('elevator')
