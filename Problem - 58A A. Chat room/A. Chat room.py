# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = int(input().strip())
# for _ in range(t):



s = input().strip()
target = list(s)
Reference = ['h', 'e', 'l', 'l', 'o']
# target = ["a", "h", "h", "e", "l", "l", "l", "l", "o", "o", "u"]

found = True  # flag to check if all elements are found
for letter in Reference:
    try:
        index = target.index(letter)
        target = target[index + 1:]  # slice from the next element
    except ValueError:
        found = False
        break

if found:
    print("YES")
else:
    print("NO")
