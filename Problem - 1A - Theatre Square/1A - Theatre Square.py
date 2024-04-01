# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
m,n,a= map(int,input().strip().split())
# print(m,n,a)
counter1 = 0
counter2 = 0
j = m//a 
k = m%a 
if k>0:
    counter1 = j + 1
else:
    counter1 = j 


x = n//a 
y = n%a 
if y>0:
    counter2 = x + 1
else:
    counter2 = x 

print(counter1*counter2)
