# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = int(input().strip())
# for _ in range(t):
#     n = int(input().strip())
#     if n%2020 == 0 or n%2020 == 1:
#         print("YES")
#     else:
#         print("NO")
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n // 2020 >= n % 2020:
        print("YES")
    else:
        print("NO")
        # '''input

# '''
# import sys
# import math
# import bisect
# from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
# from collections import defaultdict as dd
# from bisect import bisect_left as bl,bisect_right as br

# sys.setrecursionlimit(100000000)

# inp    =lambda: int(input())
# strng  =lambda: input().strip()
# jn     =lambda x,l: x.join(map(str,l))
# strl   =lambda: list(input().strip())
# mul    =lambda: map(int,input().strip().split())
# mulf   =lambda: map(float,input().strip().split())
# seq    =lambda: list(map(int,input().strip().split()))

# ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
# ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

# flush  =lambda: stdout.flush()
# stdstr =lambda: stdin.readline()
# stdint =lambda: int(stdin.readline())
# stdpr  =lambda x: stdout.write(str(x))

# mod=1000000007


# #main code

# i = input().strip()
# print(type(i))

# x = [True , True , True]
# print()