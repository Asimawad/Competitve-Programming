import sys
from collections import defaultdict
text = """below the car is a rat drinking cider and bending its elbow while this thing
is an arc that can act like a cat which cried during the night caused by pain in its
bowel"""
# #split words into list elements
wordsList = text.split()
# print(wordsList)
# #get the length of each
# lengthsList = [len(i) for i in wordsList]

d = {}
for word in wordsList:
    signature = "".join(sorted(word))
    if signature in d:
        d[signature].append(word)
    else :
        d[signature] = [word]

print([d[signature] for signature in d if len(d[signature]) > 1])