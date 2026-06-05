# exam

# 

word1 = "fried"

word2= "fired"

anagram = True


for ch in word1:#ch=f

    if word1.count(ch) != word2.count(ch):

        anagram = False

        break

print(anagram)