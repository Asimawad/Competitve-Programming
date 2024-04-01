s,n = map(int,input().split())
# print(s,n)
# n = 2
# s = 2
dragons = []
for i in range(n):
    x,y = map(int,input().split())
    dragons.append((x,y))
    dragons.sort(key=lambda pair: pair[0])
    
# print(dragons)
# 2 3
# 1 100
# 4 50
# 3 400
counter = 0
for i in range(len(dragons)):
    if s > dragons[i][0]:
        s += dragons[i][1]
        counter += 1
    else:
        print("NO")
        break
if n == counter :
    
    print("YES")
        
        















