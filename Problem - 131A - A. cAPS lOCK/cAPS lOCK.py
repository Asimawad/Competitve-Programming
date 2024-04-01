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
# #main code


# for letter in listOfLetters:
#     if letter.isupper() and Word[1:].isupper():
#         print(Word.swapcase())
#         break
#     elif letter.islower() and Word[1:].isupper():
#         print(Word.swapcase())
#     else:
#         print(Word)

        
        
        

# Asim
# aSIM
# ASIM
# A
# a
# AsAi


from collections import Counter
x = input().strip()
# c = Counter(x)
# print(c)
# listOfLetters = list(x)
# print(listOfLetters)
for i in range(len(x)):
    if x[i].isupper():
        for i in x[0:]:
            if i.isupper():
                continue
            else:
                
                break
            
    else:
        




















    
# [x.to]
# checkList = [v.isupper() for v in listOfLetters]
# upp = checkList.count(True)
# lwr = checkList.count(False)
# Total = len(checkList)
# print(checkList,upp,lwr,Total)
# if (x[0].islower() and upp == Total-1):
#     for i in range(len(x)):
#         if i == 0:
#             print(x[i].upper(), end="")
#         else:
#             print(x[i].lower(), end="")
# elif upp == len(x):
#     for i in range(len(x)):
#         print(x[i].lower(),end="")
# else:
#     print(x)



# word = input().strip()

# # Check if all characters are uppercase or all except the first are uppercase
# if word.isupper() or (word[1:].isupper() and word[0].islower()):
#     # Swap the case for the entire string
#     fixed_word = word.swapcase()
# else:
#     # Leave the word unchanged
#     fixed_word = word

# print(fixed_word)







# caps_lock_on1 = [True,True]
# caps_lock_on2 = [False,True]


# if checkList == caps_lock_on1 or checkList == caps_lock_on2 or len(Word) == 1:
#     print(Word.swapcase())
# else:
#     print(Word)

# def fix_caps_lock(word):
#     # If all letters are uppercase or all except for the first one are uppercase, swap case
#     if word.isupper() or word[1:].isupper():
#         return word.swapcase()
#     # Otherwise, return the word as is
#     return word
# print(fix_caps_lock(Word))
