import math
T = int(input())
for x in range(0,T):
    N, M = list(map(int,input().split()))
    print(math.factorial(M+N-2)//(math.factorial(N-1)*math.factorial(M-1)))