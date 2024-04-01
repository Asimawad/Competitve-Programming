# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = input().strip()

# A. Translation
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: a berlandish word differs from a birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. For example, a Berlandish word code corresponds to a Birlandish word edoc. However, it's easy to make a mistake during the «translation». Vasya translated word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

# Input
# The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters. The input data do not consist unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

# Output
# If the word t is a word s, written reversely, print YES, otherwise print NO.




import sys

Berland = list(input().strip())
Birland = list(input().strip())
reversed_Birland = Birland[::-1]

if Berland == reversed_Birland:
    print("YES")
else:
    print("NO")




# print(Birland)

