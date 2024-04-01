# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = int(input().strip())


n = int(input().strip())
forces = []
for i in range(n):
    l= list(map(int,input().strip().split()))
    forces.append(l)



summed_list = [sum(values) for values in zip(*forces)]
        
    
    
if summed_list == [0,0,0]:
    print("YES")
else:
    print("NO")
# print(summed_list)













