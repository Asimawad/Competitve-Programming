# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = int(input().strip())

n,m = map(int,input().split())
TVs  = list(map(int, input().split()))
TVs.sort()
# print(TVs)
counter = 0
for i in TVs:
    if i <= 0 and m>0:
        counter -= i
        m -= 1
    else:
        break

print(counter)





